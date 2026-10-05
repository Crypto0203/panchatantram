import re

file_path = r'C:\Users\Suresh\.gemini\antigravity-ide\scratch\panchatantra-dashboard\src\main.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_modal = '''function openEpisodeModal(id) {
  const ep = episodes.find(e => e.id === id);
  if (!ep) return;
  const modal = document.getElementById('epModal');
  const title = document.getElementById('modalEpTitle');
  const body = document.getElementById('modalEpBody');

  title.textContent = `EP ${ep.id < 10 ? '0' + ep.id : ep.id} — ${ep.title}`;
  
  let clipsHtml = '';
  if (ep.clips) {
    ep.clips.forEach(c => {
      clipsHtml += `
        <div style="background: rgba(0,0,0,0.4); border: 1px solid var(--border-subtle); border-radius: var(--radius-sm); padding: 1rem; margin-bottom: 1rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-weight: 800; color: #fff; font-size: 0.95rem;">🎬 CLIP ${c.clipNumber}</span>
            <span class="clip-badge-time">${c.timeRange}</span>
          </div>
          <div style="font-size: 0.82rem; font-weight: 700; color: var(--secondary); margin-bottom: 0.5rem;">${c.purpose}</div>

          <div style="margin-bottom: 0.5rem;">
            <div style="font-size: 0.72rem; color: var(--text-muted); font-weight: 700;">🎙️ TELUGU SPOKEN VOICEOVER:</div>
            <div style="font-size: 0.85rem; color: #a5f3fc; line-height: 1.4;">${c.teluguVO}</div>
          </div>

          <div style="margin-bottom: 0.5rem;">
            <div style="font-size: 0.72rem; color: var(--text-muted); font-weight: 700;">💬 ENGLISH SUBTITLES:</div>
            <div style="font-size: 0.82rem; color: #ffeb3b; font-weight: 600;">${c.englishSub}</div>
          </div>

          <div style="margin-bottom: 0.5rem;">
            <div style="font-size: 0.72rem; color: var(--text-muted); font-weight: 700;">🎨 AI VISUAL PROMPT (9:16):</div>
            <div style="font-family: var(--font-mono); font-size: 0.75rem; color: #cbd5e1;">${c.visualPrompt}</div>
          </div>

          <div>
            <div style="font-size: 0.72rem; color: var(--text-muted); font-weight: 700;">🔊 SOUND FOLEY & MUSIC:</div>
            <div style="font-size: 0.75rem; color: var(--accent-amber);">${c.sfx}</div>
          </div>
        </div>
      `;
    });
  }

  body.innerHTML = `
    <div style="display: flex; gap: 0.5rem; margin-bottom: 1rem; flex-wrap: wrap;">
      <span class="ep-status ${ep.status}">${ep.status}</span>
      <span class="filter-pill">${ep.category}</span>
      <span class="filter-pill">Characters: ${ep.characters}</span>
      <span class="filter-pill">Moral: ${ep.moral}</span>
    </div>

    <h4 style="color: #fff; font-size: 1.05rem; margin-bottom: 0.75rem;">📜 Complete 3 × 10s Production Script (30 Seconds):</h4>
    ${clipsHtml}

    <div style="margin-top: 1rem; text-align: right;">
      <button class="btn-primary" id="btnModalCopyAll" style="padding: 0.45rem 1rem;">
        <span>📋</span> Copy Full Episode Script
      </button>
    </div>
  `;

  modal.classList.add('active');

  document.getElementById('btnModalCopyAll')?.addEventListener('click', () => {
    sound.playPop();
    let text = `=================================================================\nPANCHATANTRA KIDS — EPISODE ${ep.id < 10 ? '0' + ep.id : ep.id}: ${ep.title}\nCOMPLETE 30-SECOND PRODUCTION SCRIPT (3 CLIPS × 10s)\n=================================================================\n\n`;
    ep.clips.forEach(c => {
      text += `[${c.clipNumber}] ${c.timeRange} — ${c.purpose}\n`;
      text += `🎙️ TELUGU VO   : ${c.teluguVO}\n`;
      text += `💬 ENGLISH SUB : ${c.englishSub}\n`;
      text += `🎨 VISUAL      : ${c.visualPrompt}\n`;
      text += `🔊 SFX / MUSIC : ${c.sfx}\n\n`;
    });
    navigator.clipboard.writeText(text);
    alert(`✅ Complete Production Script for EP ${ep.id} copied to clipboard!`);
  });

  document.getElementById('modalCloseBtn').onclick = () => {
    modal.classList.remove('active');
  };
  modal.onclick = (e) => {
    if (e.target === modal) modal.classList.remove('active');
  };
}'''

# Replace openEpisodeModal
content = re.sub(r'function openEpisodeModal\(id\) \{[\s\S]*?modal\.onclick = \(e\) => \{[\s\S]*?\};\s*\}', new_modal, content)

# Update worksheet template to format 3 x 10s
new_ws_func = '''  function updateWorksheet(epId) {
    const ep = episodes.find(e => e.id === epId) || episodes[0];
    let clipsSection = '';
    if (ep.clips) {
      ep.clips.forEach(c => {
        clipsSection += `-----------------------------------------------------------------
[CLIP ${c.clipNumber}] ${c.timeRange} — ${c.purpose}
-----------------------------------------------------------------
🎙️ TELUGU VOICEOVER:
${c.teluguVO}

💬 ENGLISH SUBTITLES:
${c.englishSub}

🎨 AI VISUAL PROMPT (9:16 VERTICAL):
${c.visualPrompt}

🔊 SOUND FOLEY & MUSIC:
${c.sfx}

`;
      });
    }

    const text = `=================================================================
PANCHATANTRA KIDS — DAILY PRODUCTION SCRIPT & WORKSHEET
=================================================================
EPISODE NUMBER : EPISODE ${ep.id < 10 ? '0' + ep.id : ep.id} OF 100
STORY TITLE    : ${ep.title}
LEAD CHARACTERS: ${ep.characters}
CATEGORY/THEME : ${ep.category}
TOTAL RUNTIME  : EXACTLY 30.0 SECONDS (3 CLIPS × 10.0s)
MORAL LESSON   : "${ep.moral}"

=================================================================
MASTER 3 × 10-SECOND SHOT-BY-SHOT SCRIPT
=================================================================

${clipsSection}=================================================================
ENGAGEMENT & GROWTH TRIGGERS
=================================================================
💬 VIEWER COMMENT POLL: "${ep.commentQ}"
🔔 NEXT EPISODE TEASER: "${ep.teaserEn}"
🏷️ TAGS: #PanchatantraKids #TeluguStories #KidsStories #MoralStories #Reels #Shorts`;

    content.textContent = text;
  }'''

content = re.sub(r'function updateWorksheet\(epId\) \{[\s\S]*?content\.textContent = text;\s*\}', new_ws_func, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated openEpisodeModal and updateWorksheet in main.js successfully!")
