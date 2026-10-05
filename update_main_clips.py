import re

file_path = r'C:\Users\Suresh\.gemini\antigravity-ide\scratch\panchatantra-dashboard\src\main.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace setSimulatorEpisode to render clips
new_set_sim = '''function setSimulatorEpisode(id) {
  const ep = episodes.find(e => e.id === id) || episodes[0];
  currentSimEp = ep;
  document.getElementById('simTopPill').textContent = `Panchatantra Tales • Part ${ep.id} of 100`;
  document.getElementById('simTitle').textContent = ep.title;
  
  // Teaser details
  const nextEp = episodes.find(e => e.id === ep.nextEpId) || ep;
  document.getElementById('simTeaserTitle').textContent = `EP ${nextEp.id}: ${nextEp.title}`;
  document.getElementById('simTeaserPrompt').textContent = ep.teaserEn;
  document.getElementById('simFollowBtn').innerHTML = `<span>🔔</span> FOLLOW FOR EP ${nextEp.id}`;
  
  renderSimClipsGrid(ep);
  updateSimulatorDisplay();
}

function renderSimClipsGrid(ep) {
  const grid = document.getElementById('simClipsGrid');
  if (!grid || !ep.clips) return;
  
  grid.innerHTML = '';
  ep.clips.forEach((clip, idx) => {
    const card = document.createElement('div');
    card.className = 'clip-card';
    card.id = `simClipCard_${idx}`;
    card.innerHTML = `
      <div>
        <div class="clip-card-header">
          <span style="font-weight: 800; font-size: 0.95rem; color: #fff;">CLIP ${clip.clipNumber}</span>
          <span class="clip-badge-time">${clip.timeRange}</span>
        </div>
        <div class="clip-purpose">${clip.purpose}</div>

        <div class="clip-box-section">
          <div class="clip-box-title">🎙️ Telugu Spoken Voiceover:</div>
          <div class="clip-telugu-text">${clip.teluguVO}</div>
        </div>

        <div class="clip-box-section">
          <div class="clip-box-title">💬 English Subtitles:</div>
          <div class="clip-english-text">${clip.englishSub}</div>
        </div>

        <div class="clip-box-section">
          <div class="clip-box-title">🎨 AI Visual Prompt (9:16):</div>
          <div class="clip-prompt-text">${clip.visualPrompt}</div>
        </div>

        <div class="clip-box-section">
          <div class="clip-box-title">🔊 Sound Foley & Music:</div>
          <div class="clip-sfx-text">${clip.sfx}</div>
        </div>
      </div>
      <div style="margin-top: 0.75rem; text-align: right;">
        <button class="btn-secondary btn-copy-clip" data-idx="${idx}" style="padding: 0.3rem 0.65rem; font-size: 0.75rem;">
          <span>📋</span> Copy Clip ${clip.clipNumber}
        </button>
      </div>
    `;
    grid.appendChild(card);
  });

  grid.querySelectorAll('.btn-copy-clip').forEach(btn => {
    btn.addEventListener('click', (e) => {
      sound.playPop();
      const idx = parseInt(e.currentTarget.dataset.idx);
      const c = ep.clips[idx];
      const clipText = `CLIP ${c.clipNumber} (${c.timeRange})\nPURPOSE: ${c.purpose}\nTELUGU VO: ${c.teluguVO}\nENGLISH SUB: ${c.englishSub}\nVISUAL PROMPT: ${c.visualPrompt}\nSFX: ${c.sfx}`;
      navigator.clipboard.writeText(clipText);
      alert(`✅ Clip ${c.clipNumber} Script copied!`);
    });
  });

  document.getElementById('btnCopyFullScript')?.addEventListener('click', () => {
    sound.playPop();
    let fullScript = `=================================================================\nPANCHATANTRA KIDS — EPISODE ${ep.id < 10 ? '0' + ep.id : ep.id}: ${ep.title}\nCOMPLETE 30-SECOND SCRIPT (3 CLIPS × 10s)\n=================================================================\n\n`;
    ep.clips.forEach(c => {
      fullScript += `[${c.clipNumber}] ${c.timeRange} — ${c.purpose}\n`;
      fullScript += `🎙️ TELUGU VO   : ${c.teluguVO}\n`;
      fullScript += `💬 ENGLISH SUB : ${c.englishSub}\n`;
      fullScript += `🎨 VISUAL      : ${c.visualPrompt}\n`;
      fullScript += `🔊 SFX / MUSIC : ${c.sfx}\n\n`;
    });
    navigator.clipboard.writeText(fullScript);
    alert(`✅ Complete 3-Clip Production Script for EP ${ep.id} copied to clipboard!`);
  });
}'''

# Replace in content
content = re.sub(r'function setSimulatorEpisode\(id\) \{[\s\S]*?updateSimulatorDisplay\(\);\s*\}', new_set_sim, content)

# Update updateSimulatorDisplay to highlight active card
highlight_logic = '''  // Highlight active 10s clip card
  const activeClipIdx = simTime < 10.0 ? 0 : (simTime < 20.0 ? 1 : 2);
  for (let i = 0; i < 3; i++) {
    const card = document.getElementById(`simClipCard_${i}`);
    if (card) {
      if (i === activeClipIdx) {
        card.classList.add('active-clip');
      } else {
        card.classList.remove('active-clip');
      }
    }
  }'''

# Insert highlight_logic inside updateSimulatorDisplay
content = content.replace("scrubber.value = simTime;", "scrubber.value = simTime;\n" + highlight_logic)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated main.js with 3 x 10s production script cards!")
