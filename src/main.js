import { episodes } from './episodes.js';
import { verifyVaultPin, isVaultUnlocked, lockVault } from './auth.js';
import { sound } from './audio.js';

// Application State
let currentPin = '';
let currentSimEp = episodes[0];
let simPlaying = false;
let simTime = 0;
let simInterval = null;
let lastSfxTriggered = -1;

// Elements
const lockScreen = document.getElementById('lockScreen');
const pinDisplay = document.getElementById('pinDisplay');
const vaultFeedback = document.getElementById('vaultFeedback');
const keypad = document.getElementById('keypad');
const btnLockVault = document.getElementById('btnLockVault');

// Init Check
document.addEventListener('DOMContentLoaded', () => {
  if (isVaultUnlocked()) {
    lockScreen.classList.add('hidden');
  } else {
    lockScreen.classList.remove('hidden');
  }
  initKeypad();
  initNavigation();
  initSimulator();
  initEpisodesHub();
  initWorksheetTab();
  initExport();
});

/* ==========================================================================
   PIN VAULT SECURITY LOGIC
   ========================================================================== */

function initKeypad() {
  keypad.addEventListener('click', (e) => {
    const btn = e.target.closest('.key-btn');
    if (!btn) return;
    sound.playPop();
    const key = btn.dataset.key;
    handleKeyInput(key);
  });

  // Physical keyboard support
  window.addEventListener('keydown', (e) => {
    if (lockScreen.classList.contains('hidden')) return;
    if (e.key >= '0' && e.key <= '9') {
      sound.playPop();
      handleKeyInput(e.key);
    } else if (e.key === 'Backspace') {
      sound.playPop();
      handleKeyInput('back');
    } else if (e.key === 'Escape' || e.key === 'Delete') {
      handleKeyInput('clear');
    }
  });

  btnLockVault.addEventListener('click', () => {
    lockVault();
    currentPin = '';
    updatePinDots();
    vaultFeedback.textContent = 'Vault Locked. Enter PIN to resume.';
    vaultFeedback.className = 'vault-feedback';
    lockScreen.classList.remove('hidden');
    sound.playPop();
  });
}

async function handleKeyInput(key) {
  if (key === 'clear') {
    currentPin = '';
    updatePinDots();
    vaultFeedback.textContent = 'PIN cleared.';
    vaultFeedback.className = 'vault-feedback';
    return;
  }
  if (key === 'back') {
    currentPin = currentPin.slice(0, -1);
    updatePinDots();
    return;
  }
  if (currentPin.length < 4) {
    currentPin += key;
    updatePinDots();
    if (currentPin.length === 4) {
      vaultFeedback.textContent = 'Verifying cryptographic digest...';
      vaultFeedback.className = 'vault-feedback';
      
      const success = await verifyVaultPin(currentPin);
      if (success) {
        sound.playFanfare();
        vaultFeedback.textContent = '✅ Access Granted! Unlocking vault...';
        vaultFeedback.className = 'vault-feedback success';
        
        setTimeout(() => {
          lockScreen.classList.add('hidden');
          currentPin = '';
          updatePinDots();
        }, 500);
      } else {
        sound.playBoing();
        vaultFeedback.textContent = '❌ Invalid PIN. Access Denied.';
        vaultFeedback.className = 'vault-feedback error';
        
        // Shake dots
        for (let i = 0; i < 4; i++) {
          const dot = document.getElementById(`dot${i}`);
          if (dot) dot.classList.add('error');
        }
        setTimeout(() => {
          currentPin = '';
          updatePinDots();
        }, 600);
      }
    }
  }
}

function updatePinDots() {
  for (let i = 0; i < 4; i++) {
    const dot = document.getElementById(`dot${i}`);
    if (dot) {
      dot.className = 'pin-dot';
      if (i < currentPin.length) {
        dot.classList.add('filled');
      }
    }
  }
}

/* ==========================================================================
   NAVIGATION
   ========================================================================== */

function initNavigation() {
  const tabs = document.querySelectorAll('.nav-tab-btn');
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      sound.playPop();
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      const targetId = `pane-${tab.dataset.tab}`;
      document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
      const targetPane = document.getElementById(targetId);
      if (targetPane) targetPane.classList.add('active');
    });
  });

  // Hero Quick action buttons
  document.getElementById('btnLaunchSim')?.addEventListener('click', () => {
    document.querySelector('[data-tab="simulator"]').click();
  });
  document.getElementById('btnExploreEpisodes')?.addEventListener('click', () => {
    document.querySelector('[data-tab="episodes"]').click();
  });
}

/* ==========================================================================
   30-SECOND REEL SIMULATOR
   ========================================================================== */

function initSimulator() {
  const select = document.getElementById('simEpSelect');
  episodes.forEach(ep => {
    const opt = document.createElement('option');
    opt.value = ep.id;
    opt.textContent = `EP ${ep.id < 10 ? '0' + ep.id : ep.id} — ${ep.title} (${ep.characters})`;
    select.appendChild(opt);
  });

  select.addEventListener('change', (e) => {
    const epId = parseInt(e.target.value);
    setSimulatorEpisode(epId);
  });

  const btnPlay = document.getElementById('btnSimPlay');
  const btnRestart = document.getElementById('btnSimRestart');
  const btnNext = document.getElementById('btnSimNext');
  const scrubber = document.getElementById('simScrubber');
  const btnSound = document.getElementById('btnToggleSound');

  btnPlay.addEventListener('click', toggleSimulatorPlayback);
  btnRestart.addEventListener('click', resetSimulator);
  btnNext.addEventListener('click', () => {
    let nextId = currentSimEp.id + 1;
    if (nextId > episodes.length) nextId = 1;
    select.value = nextId;
    setSimulatorEpisode(nextId);
    resetSimulator();
    startSimulatorPlayback();
  });

  scrubber.addEventListener('input', (e) => {
    simTime = parseFloat(e.target.value);
    updateSimulatorDisplay();
  });

  btnSound.addEventListener('click', () => {
    sound.muted = !sound.muted;
    const icon = document.getElementById('soundIcon');
    const label = document.getElementById('soundLabel');
    if (sound.muted) {
      icon.textContent = '🔇';
      label.textContent = 'Muted';
    } else {
      icon.textContent = '🔊';
      label.textContent = 'Sound ON';
      sound.playPop();
    }
  });

  setSimulatorEpisode(1);
}

function setSimulatorEpisode(id) {
  const ep = episodes.find(e => e.id === id) || episodes[0];
  currentSimEp = ep;
  document.getElementById('simTopPill').textContent = `Panchatantra Tales • Part ${ep.id} of 100`;
  document.getElementById('simTitle').textContent = ep.title;
  
  // Teaser details
  const nextEp = episodes.find(e => e.id === ep.nextEpId) || ep;
  document.getElementById('simTeaserTitle').textContent = `EP ${nextEp.id}: ${nextEp.title}`;
  document.getElementById('simTeaserPrompt').textContent = ep.teaserEn;
  document.getElementById('simFollowBtn').innerHTML = `<span>🔔</span> FOLLOW FOR EP ${nextEp.id}`;
  
  updateSimulatorDisplay();
}

function toggleSimulatorPlayback() {
  if (simPlaying) {
    pauseSimulatorPlayback();
  } else {
    startSimulatorPlayback();
  }
}

function startSimulatorPlayback() {
  simPlaying = true;
  sound.init();
  document.getElementById('playIcon').textContent = '⏸️';
  document.getElementById('playText').textContent = 'Pause Reel';
  document.getElementById('simBg').classList.add('zooming');
  
  simInterval = setInterval(() => {
    simTime += 0.2;
    if (simTime >= 30) {
      simTime = 30;
      pauseSimulatorPlayback();
    }
    updateSimulatorDisplay();
  }, 200);
}

function pauseSimulatorPlayback() {
  simPlaying = false;
  clearInterval(simInterval);
  document.getElementById('playIcon').textContent = '▶️';
  document.getElementById('playText').textContent = 'Play Reel (30s)';
  document.getElementById('simBg').classList.remove('zooming');
}

function resetSimulator() {
  pauseSimulatorPlayback();
  simTime = 0;
  lastSfxTriggered = -1;
  updateSimulatorDisplay();
}

function updateSimulatorDisplay() {
  const scrubber = document.getElementById('simScrubber');
  const timeDisplay = document.getElementById('simTimeDisplay');
  const beatIndicator = document.getElementById('simBeatIndicator');
  const beatBadge = document.getElementById('simBeatBadge');
  const visualCue = document.getElementById('simVisualCue');
  const subText = document.getElementById('simSubtitleText');
  const teluguVoice = document.getElementById('simTeluguVoice');
  const teaserOverlay = document.getElementById('simTeaserOverlay');

  scrubber.value = simTime;
  const secs = Math.floor(simTime);
  const ms = Math.floor((simTime % 1) * 10);
  timeDisplay.textContent = `00:${secs < 10 ? '0' + secs : secs}.${ms} / 00:30.0`;

  // Precision 5 Micro-Beats Mapping
  if (simTime < 3.0) {
    // Beat 1: Thumb-Stopper Hook
    beatBadge.className = 'beat-badge hook';
    beatBadge.textContent = '0–3s: Thumb-Stopper Hook';
    beatIndicator.textContent = 'Beat 1: Thumb-Stopper Hook (0–3s)';
    visualCue.textContent = `⚡ IN-MEDIA-RES: ${currentSimEp.leadChar} in extreme peril!`;
    subText.textContent = `"${currentSimEp.hookEn}"`;
    teluguVoice.textContent = `"${currentSimEp.hookTe}"`;
    teaserOverlay.style.display = 'none';

    if (lastSfxTriggered < 1 && simPlaying) {
      sound.playWhoosh();
      sound.playBoing();
      lastSfxTriggered = 1;
    }
  } else if (simTime < 8.0) {
    // Beat 2: Setup & Stakes
    beatBadge.className = 'beat-badge setup';
    beatBadge.textContent = '3–8s: Setup & Stakes';
    beatIndicator.textContent = 'Beat 2: Setup & Stakes (3–8s)';
    visualCue.textContent = `📖 Magic storybook transition → ${currentSimEp.characters} world`;
    subText.textContent = `"${currentSimEp.beat1}"`;
    teluguVoice.textContent = `"కథ మొదలైంది... కానీ అక్కడ పెద్ద చిక్కు వచ్చిపడింది!"`;
    teaserOverlay.style.display = 'none';

    if (lastSfxTriggered < 2 && simPlaying) {
      sound.playPop();
      lastSfxTriggered = 2;
    }
  } else if (simTime < 18.0) {
    // Beat 3: Crisis & Trap
    beatBadge.className = 'beat-badge crisis';
    beatBadge.textContent = '8–18s: Crisis & Trap';
    beatIndicator.textContent = 'Beat 3: Crisis & Trap (8–18s)';
    visualCue.textContent = `⚠️ The villain closes in! Protagonist trapped!`;
    subText.textContent = `"${currentSimEp.beat2}"`;
    teluguVoice.textContent = `"అపాయం చుట్టుముట్టింది... బయటపడే దారి లేదు!"`;
    teaserOverlay.style.display = 'none';

    if (lastSfxTriggered < 3 && simPlaying) {
      sound.playTension();
      lastSfxTriggered = 3;
    }
  } else if (simTime < 25.0) {
    // Beat 4: Brains-over-Brawn Twist
    beatBadge.className = 'beat-badge climax';
    beatBadge.textContent = '18–25s: Clever Twist';
    beatIndicator.textContent = 'Beat 4: Clever Twist & Victory (18–25s)';
    visualCue.textContent = `💡 Genius trick triggers! Brain wins over brawn!`;
    subText.textContent = `"${currentSimEp.beat3} Moral: ${currentSimEp.moral}"`;
    teluguVoice.textContent = `"ఉపాయంతో అపాయాన్ని దాటేశారు! ${currentSimEp.moral}"`;
    teaserOverlay.style.display = 'none';

    if (lastSfxTriggered < 4 && simPlaying) {
      sound.playFanfare();
      lastSfxTriggered = 4;
    }
  } else {
    // Beat 5: Moral + NEXT EPISODE TEASER (25-30s)
    beatBadge.className = 'beat-badge teaser';
    beatBadge.textContent = '25–30s: Sneak Peek & Follow';
    beatIndicator.textContent = 'Beat 5: BINGE TEASER & FOLLOW (25–30s)';
    visualCue.textContent = `🔔 TOMORROW TEASER: ${currentSimEp.nextEpTitle}!`;
    subText.textContent = `"${currentSimEp.teaserEn}"`;
    teluguVoice.textContent = `"${currentSimEp.teaserTe}"`;
    
    // Pop up Sneak Peek Teaser Overlay
    teaserOverlay.style.display = 'flex';

    if (lastSfxTriggered < 5 && simPlaying) {
      sound.playBell();
      lastSfxTriggered = 5;
    }
  }
}

/* ==========================================================================
   100-EPISODE MASTER HUB
   ========================================================================= */

function initEpisodesHub() {
  const grid = document.getElementById('episodesGrid');
  const searchInput = document.getElementById('epSearchInput');
  const batchButtons = document.querySelectorAll('#batchFilters .filter-pill');
  const countDisplay = document.getElementById('epCountDisplay');

  let activeBatch = 'all';
  let searchQuery = '';

  function renderGrid() {
    grid.innerHTML = '';
    const filtered = episodes.filter(ep => {
      const matchSearch = ep.title.toLowerCase().includes(searchQuery) ||
                          ep.characters.toLowerCase().includes(searchQuery) ||
                          ep.moral.toLowerCase().includes(searchQuery);
      let matchBatch = true;
      if (activeBatch === '1') matchBatch = ep.id >= 1 && ep.id <= 25;
      else if (activeBatch === '2') matchBatch = ep.id >= 26 && ep.id <= 50;
      else if (activeBatch === '3') matchBatch = ep.id >= 51 && ep.id <= 75;
      else if (activeBatch === '4') matchBatch = ep.id >= 76 && ep.id <= 100;

      return matchSearch && matchBatch;
    });

    countDisplay.textContent = filtered.length;

    filtered.forEach(ep => {
      const card = document.createElement('div');
      card.className = 'episode-card';
      card.innerHTML = `
        <div>
          <div class="ep-header">
            <span class="ep-badge">EP ${ep.id < 10 ? '0' + ep.id : ep.id}</span>
            <span class="ep-status ${ep.status}">${ep.status}</span>
          </div>
          <h3 class="ep-title">${ep.title}</h3>
          <div class="ep-chars">🐾 ${ep.characters} • ${ep.category}</div>
          
          <div class="ep-hook-box">
            <strong>🎯 3s Hook:</strong> ${ep.hookEn}
          </div>

          <div class="ep-teaser-box">
            <strong>🔗 Tomorrow in EP ${ep.nextEpId}:</strong> ${ep.teaserEn}
          </div>
        </div>

        <div class="ep-card-actions">
          <button class="btn-primary btn-play-ep" data-id="${ep.id}" style="padding: 0.4rem 0.8rem; font-size: 0.78rem;">
            <span>▶️</span> Test in Player
          </button>
          <button class="btn-secondary btn-view-script" data-id="${ep.id}" style="padding: 0.4rem 0.75rem; font-size: 0.78rem;">
            <span>📋</span> View Script
          </button>
        </div>
      `;
      grid.appendChild(card);
    });

    // Wire Card Buttons
    grid.querySelectorAll('.btn-play-ep').forEach(btn => {
      btn.addEventListener('click', (e) => {
        sound.playPop();
        const epId = parseInt(e.currentTarget.dataset.id);
        const sel = document.getElementById('simEpSelect');
        sel.value = epId;
        setSimulatorEpisode(epId);
        document.querySelector('[data-tab="simulator"]').click();
        resetSimulator();
        startSimulatorPlayback();
      });
    });

    grid.querySelectorAll('.btn-view-script').forEach(btn => {
      btn.addEventListener('click', (e) => {
        sound.playPop();
        const epId = parseInt(e.currentTarget.dataset.id);
        openEpisodeModal(epId);
      });
    });
  }

  searchInput.addEventListener('input', (e) => {
    searchQuery = e.target.value.toLowerCase().trim();
    renderGrid();
  });

  batchButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      sound.playPop();
      batchButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeBatch = btn.dataset.batch;
      renderGrid();
    });
  });

  renderGrid();
}

/* ==========================================================================
   EPISODE SCRIPT MODAL
   ========================================================================== */

function openEpisodeModal(id) {
  const ep = episodes.find(e => e.id === id);
  if (!ep) return;
  const modal = document.getElementById('epModal');
  const title = document.getElementById('modalEpTitle');
  const body = document.getElementById('modalEpBody');

  title.textContent = `EP ${ep.id < 10 ? '0' + ep.id : ep.id} — ${ep.title}`;
  body.innerHTML = `
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem;">
      <span class="ep-status ${ep.status}">${ep.status}</span>
      <span class="filter-pill">${ep.category}</span>
      <span class="filter-pill">Characters: ${ep.characters}</span>
    </div>

    <div style="background: rgba(0,0,0,0.3); padding: 1rem; border-radius: var(--radius-sm); margin-bottom: 1rem;">
      <h4 style="color: #fff; font-size: 0.95rem; margin-bottom: 0.5rem;">🎯 3-Second Action Hook (Thumb-Stopper):</h4>
      <p style="color: #fca5a5; font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>English:</strong> "${ep.hookEn}"</p>
      <p style="color: #a5f3fc; font-size: 0.85rem;"><strong>Telugu VO:</strong> "${ep.hookTe}"</p>
    </div>

    <div style="background: rgba(0,0,0,0.3); padding: 1rem; border-radius: var(--radius-sm); margin-bottom: 1rem;">
      <h4 style="color: #fff; font-size: 0.95rem; margin-bottom: 0.5rem;">🎬 3-Beat Narrative Arc:</h4>
      <p style="font-size: 0.85rem; margin-bottom: 0.35rem;"><strong>Clip 1 (0–10s):</strong> ${ep.beat1}</p>
      <p style="font-size: 0.85rem; margin-bottom: 0.35rem;"><strong>Clip 2 (10–20s):</strong> ${ep.beat2}</p>
      <p style="font-size: 0.85rem;"><strong>Clip 3 (20–25s):</strong> ${ep.beat3}</p>
    </div>

    <div style="background: rgba(6, 182, 212, 0.1); border-left: 3px solid var(--secondary); padding: 1rem; border-radius: var(--radius-sm); margin-bottom: 1rem;">
      <h4 style="color: #fff; font-size: 0.95rem; margin-bottom: 0.5rem;">🔗 Next Episode Sneak Peek (26–30s):</h4>
      <p style="color: #e2e8f0; font-size: 0.85rem; margin-bottom: 0.35rem;"><strong>English:</strong> "${ep.teaserEn}"</p>
      <p style="color: #a5f3fc; font-size: 0.85rem;"><strong>Telugu VO:</strong> "${ep.teaserTe}"</p>
    </div>

    <div style="background: rgba(0,0,0,0.3); padding: 1rem; border-radius: var(--radius-sm);">
      <h4 style="color: #fff; font-size: 0.95rem; margin-bottom: 0.5rem;">🤖 3D Pixar Midjourney Prompt:</h4>
      <div style="font-family: var(--font-mono); font-size: 0.78rem; color: #a5f3fc; word-break: break-all;">
        ${ep.prompt}
      </div>
    </div>
  `;

  modal.classList.add('active');
  document.getElementById('modalCloseBtn').onclick = () => {
    modal.classList.remove('active');
  };
  modal.onclick = (e) => {
    if (e.target === modal) modal.classList.remove('active');
  };
}

/* ==========================================================================
   DAILY WORKSHEET TAB
   ========================================================================== */

function initWorksheetTab() {
  const sel = document.getElementById('worksheetEpSelect');
  const content = document.getElementById('worksheetContent');

  episodes.forEach(ep => {
    const opt = document.createElement('option');
    opt.value = ep.id;
    opt.textContent = `EP ${ep.id < 10 ? '0' + ep.id : ep.id}: ${ep.title}`;
    sel.appendChild(opt);
  });

  function updateWorksheet(epId) {
    const ep = episodes.find(e => e.id === epId) || episodes[0];
    const text = `=================================================================
PANCHATANTRA KIDS — DAILY EPISODE PRODUCTION WORKSHEET
=================================================================
EPISODE NUMBER : EPISODE ${ep.id < 10 ? '0' + ep.id : ep.id} OF 100
STORY TITLE    : ${ep.title}
LEAD CHARACTERS: ${ep.characters}
CATEGORY/THEME : ${ep.category}
TARGET RUNTIME : 30.0 SECONDS (3 CLIPS × 10s)

-----------------------------------------------------------------
1. 🎯 3-SECOND ACTION HOOK (THUMB-STOPPER)
-----------------------------------------------------------------
Visual Action : Extreme push-in on ${ep.leadChar} facing immediate peril!
English Sub   : "${ep.hookEn}"
Telugu VO     : "${ep.hookTe}"
Sound Foley   : Cartoon Gasp + Dramatic Whoosh Sting

-----------------------------------------------------------------
2. 🎬 30-SECOND MICRO-BEAT TIMELINE
-----------------------------------------------------------------
Clip 1 (0–10s)  : ${ep.beat1}
Clip 2 (10–20s) : ${ep.beat2}
Clip 3 (20–25s) : ${ep.beat3}
Moral Takeaway  : "${ep.moral}"

-----------------------------------------------------------------
3. 🔗 NEXT EPISODE SNEAK PEEK & BINGE-FOLLOW ENGINE (26–30s)
-----------------------------------------------------------------
Next Episode   : EP ${ep.nextEpId} — ${ep.nextEpTitle}
Teaser Hook    : "${ep.teaserEn}"
Telugu Teaser  : "${ep.teaserTe}"
Visual Overlay : Bouncing 3D Follow Button + Bell Ring SFX

-----------------------------------------------------------------
4. 🤖 AI GENERATION PROMPT (MIDJOURNEY / RUNWAY GEN-3)
-----------------------------------------------------------------
${ep.prompt}

-----------------------------------------------------------------
5. 💬 VIEWER COMMENT POLL TRIGGER
-----------------------------------------------------------------
Comment Poll   : "${ep.commentQ}"
Hashtags       : #PanchatantraKids #TeluguStories #KidsCartoons #MoralStories #Reels`;

    content.textContent = text;
  }

  sel.addEventListener('change', (e) => {
    updateWorksheet(parseInt(e.target.value));
  });

  document.getElementById('btnCopyWorksheet').addEventListener('click', () => {
    sound.playPop();
    navigator.clipboard.writeText(content.textContent);
    alert('✅ Daily Episode Worksheet copied to clipboard!');
  });

  document.getElementById('btnDownloadWorksheet').addEventListener('click', () => {
    sound.playPop();
    const epId = parseInt(sel.value);
    const blob = new Blob([content.textContent], { type: 'text/markdown;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `Panchatantra_EP_${epId < 10 ? '0' + epId : epId}_Worksheet.md`;
    a.click();
    URL.revokeObjectURL(url);
  });

  document.getElementById('btnCopyPrompt')?.addEventListener('click', () => {
    sound.playPop();
    const promptText = document.getElementById('masterPromptBox').textContent.trim();
    navigator.clipboard.writeText(promptText);
    alert('✅ Master 3D Animation Prompt copied to clipboard!');
  });

  updateWorksheet(1);
}

/* ==========================================================================
   EXPORT FUNCTIONALITY
   ========================================================================== */

function initExport() {
  document.getElementById('btnExportAll').addEventListener('click', () => {
    sound.playPop();
    const jsonStr = JSON.stringify(episodes, null, 2);
    const blob = new Blob([jsonStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'panchatantra_100_episodes_master_data.json';
    a.click();
    URL.revokeObjectURL(url);
  });
}
