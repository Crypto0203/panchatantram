import docx, json, re

doc = docx.Document(r'C:\Users\Suresh\Downloads\Panchatantra_Kids_100_Episode_Master_Plan.docx')
eps = []

raw_eps = []
for p in doc.paragraphs:
    text = p.text.strip()
    if text.startswith('EP '):
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        header = lines[0]
        m = re.match(r'EP\s*(\d+)\s*—\s*(.*)', header)
        num = int(m.group(1)) if m else len(raw_eps) + 1
        title = m.group(2).strip() if m else header
        
        chars = 'Animal friends'
        moral = 'Think wisely.'
        for l in lines[1:]:
            if 'Characters:' in l:
                parts = l.split('|')
                chars = parts[0].replace('🐾 Characters:', '').replace('Characters:', '').strip()
                if len(parts) > 1 and 'Moral:' in parts[1]:
                    moral = parts[1].replace('💡 Moral:', '').replace('Moral:', '').strip()
        raw_eps.append({'id': num, 'title': title, 'characters': chars, 'moral': moral})

categories = ['Wisdom & Strategy', 'Friendship & Loyalty', 'Overcoming Danger', 'Pride & Humility', 'Quick Wit', 'Patience & Unity']

for i, e in enumerate(raw_eps):
    num = e['id']
    title = e['title']
    chars = e['characters']
    moral = e['moral']
    
    lead_char = chars.split('•')[0].strip() if '•' in chars else chars.split()[0]
    next_ep = raw_eps[i+1] if i+1 < len(raw_eps) else None
    
    batch = f"Batch {(num-1)//25 + 1} (EP {((num-1)//25)*25 + 1:02d}–{min(((num-1)//25 + 1)*25, 100):02d})"
    cat = categories[(num - 1) % len(categories)]
    
    hook_en = f"Wait! Can {lead_char} escape this impossible danger before time runs out?!"
    hook_te = f"ఆగండి! ఈ {lead_char} ఇంత పెద్ద అపాయం నుండి ఎలా తప్పించుకుంటుందో తెలుసా?"
    
    beat1 = f"High-energy hook: {lead_char} encounters an unexpected crisis in the deep forest!"
    beat2 = f"The danger intensifies! Physical strength fails, and the trap closes in."
    beat3 = f"Clever twist: With lightning-fast brainpower, {lead_char} outsmarts the obstacle!"
    
    if next_ep:
        next_id = next_ep['id']
        next_title = next_ep['title']
        teaser_en = f"Tomorrow in EP {next_id:02d} ({next_title}): What secret trick saves the forest next?! Tap FOLLOW so you don't miss tomorrow's adventure!"
        teaser_te = f"మరి రేపటి కథలో ({next_title})... ఏ అద్భుతం జరిగిందో తెలుసా? రేపటి ఎపిసోడ్ కోసం ఇప్పుడే FOLLOW చేయండి!"
    else:
        next_id = 1
        next_title = "The Clever Rabbit & Hungry Fox (Season Replay)"
        teaser_en = "You completed all 100 Episodes! Stay followed for Season 2: Jataka Tales launching next week!"
        teaser_te = "100 కథలు పూర్తయ్యాయి! వచ్చే వారం వచ్చే సీజన్ 2 కోసం ఇప్పుడే FOLLOW చేసి ఉంచండి!"
        
    comment_q = f"Would YOU act like {lead_char} in this situation? Comment YES or NO!"
    
    prompt = f"3D Pixar Disney animated film style, cute expressive {lead_char}, vibrant lush jungle background, warm golden volumetric lighting, cinematic 8k render, Unreal Engine 5 --ar 9:16"
    
    eps.append({
        'id': num,
        'title': title,
        'characters': chars,
        'leadChar': lead_char,
        'moral': moral,
        'category': cat,
        'batch': batch,
        'status': 'Published' if num <= 3 else ('Ready' if num <= 15 else 'Scripted'),
        'hookEn': hook_en,
        'hookTe': hook_te,
        'beat1': beat1,
        'beat2': beat2,
        'beat3': beat3,
        'nextEpId': next_id,
        'nextEpTitle': next_title,
        'teaserEn': teaser_en,
        'teaserTe': teaser_te,
        'commentQ': comment_q,
        'prompt': prompt,
        'views': 45200 if num == 1 else (38100 if num == 2 else (29400 if num == 3 else 0)),
        'retention': 84.5 if num == 1 else (82.1 if num == 2 else (80.7 if num == 3 else 0))
    })

# EP 01 Custom Pilot
eps[0]['hookEn'] = "Wait! Can this tiny bunny really escape a hungry sly fox?!"
eps[0]['hookTe'] = "ఆగండి! ఈ బుల్లి కుందేలు ఆకలితో ఉన్న నక్క నుండి ఎలా తప్పించుకుంటుందో తెలుసా?"
eps[0]['beat1'] = "Sly Fox blocks both hollow log exits; Bunny is completely trapped!"
eps[0]['beat2'] = "Bunny braces feet and rolls the hollow log down the steep grassy hill!"
eps[0]['beat3'] = "SPLAT! Rolling log sends dizzy fox headfirst into a squishy mud puddle!"
eps[0]['moral'] = "Brain power is always stronger than sharp teeth!"
eps[0]['teaserEn'] = "Tomorrow in Ep 2: How does a clever monkey escape a river crocodile?! TAP FOLLOW NOW!"
eps[0]['teaserTe'] = "మరి రేపటి కథలో... మొసలి నోటి నుండి తెలివైన కోతి ఎలా తప్పించుకుంది? రేపటి ఎపిసోడ్ కోసం ఇప్పుడే FOLLOW చేయండి!"

# EP 02 Custom Pilot
eps[1]['hookEn'] = "OH NO! Is the clever monkey trapped in deep crocodile waters?!"
eps[1]['hookTe'] = "అయ్యో! నది మధ్యలో మొసలి నోటికి కోతి చిక్కిందా?!"
eps[1]['beat1'] = "Crocodile offers a friendly river ride, but secretly plans to take monkey's heart!"
eps[1]['beat2'] = "Monkey smiles calmly: 'Oh! But I left my sweet heart up on the berry tree!'"
eps[1]['beat3'] = "Foolish crocodile swims back; Monkey leaps high to safety and laughs!"
eps[1]['moral'] = "Stay calm and think fast when facing trouble!"
eps[1]['teaserEn'] = "Tomorrow in Ep 3: How can a tiny mouse save the mighty Jungle King?! TAP FOLLOW NOW!"
eps[1]['teaserTe'] = "మరి రేపటి కథలో... అడవి రాజు సింహాన్ని ఒక చిట్టి ఎలుక ఎలా కాపాడింది? రేపటి ఎపిసోడ్ కోసం ఇప్పుడే FOLLOW చేయండి!"

with open(r'C:\Users\Suresh\.gemini\antigravity-ide\scratch\panchatantra-dashboard\src\episodes.js', 'w', encoding='utf-8') as f:
    f.write('export const episodes = ' + json.dumps(eps, ensure_ascii=False, indent=2) + ';\n')

print(f"Exported {len(eps)} episodes to src/episodes.js successfully!")
