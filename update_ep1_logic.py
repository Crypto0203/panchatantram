import json

with open(r'C:\Users\Suresh\.gemini\antigravity-ide\scratch\panchatantra-dashboard\src\episodes.js', 'r', encoding='utf-8') as f:
    text = f.read().replace('export const episodes = ', '').rstrip(';\n')
    eps = json.loads(text)

ep1 = eps[0]
ep1['hookEn'] = "Wait! How can a tiny bunny trapped in a tree hollow escape a hungry fox?!"
ep1['hookTe'] = "ఆగండి! చెట్టు తొర్రలో చిక్కుకున్న బుల్లి కుందేలు ఆకలితో ఉన్న నక్క నుండి ఎలా తప్పించుకుంటుందో తెలుసా?"
ep1['beat1'] = "Fox blocks the tree hollow entrance, licking his lips. Rabbit is cornered inside!"
ep1['beat2'] = "Fox sticks his snout into the hole. Rabbit kicks a thick cloud of stinging sand and dry dust straight into the fox's eyes!"
ep1['beat3'] = "Blinded and sneezing, the fox stumbles blindly, trips over a huge tree root, and crashes face-first SPLAT into a wet mud puddle!"

ep1['clips'][0] = {
    "clipNumber": 1,
    "timeRange": "00:00 – 00:10 (10 Seconds)",
    "purpose": "🎯 Thumb-Stopper Hook & The Trap",
    "cameraAction": "Camera pushes in rapidly to a cute chubby brown baby bunny trapped inside the hollow root base of a massive ancient tree. A hungry red fox blocks the only exit, grinning wickedly and baring sharp teeth.",
    "visualPrompt": "3D Pixar Disney style, extreme close-up of cute chubby fluffy brown baby bunny with big expressive dark eyes trapped inside the hollow root base of an ancient banyan tree, hungry red fox with sharp teeth and sneaky grin peering directly into the hole blocking the only exit, warm volumetric jungle sunlight, 8k render, Unreal Engine 5 --ar 9:16",
    "teluguVO": "\"ఆగండి! చెట్టు తొర్రలో చిక్కుకున్న ఈ బుల్లి కుందేలు... ఆకలితో ఉన్న నక్క నుండి ఎలా తప్పించుకుందో తెలుసా? నక్క బావ తొర్ర ముందే కాపలా కాసింది... కుందేలుకు బయటకు వచ్చే దారే లేదు!\"",
    "englishSub": "\"Wait! How can a tiny bunny trapped in a tree hollow escape a hungry sly fox?! The fox blocked the only exit... Bunny was completely trapped!\"",
    "sfx": "0:01s Cartoon Gasp • 0:03s Magic Shimmer Chime • 0:06s Sneaky Fox Tiptoe Steps • 0:09s Low Tension Cello Sting"
}

ep1['clips'][1] = {
    "clipNumber": 2,
    "timeRange": "00:10 – 00:20 (10 Seconds)",
    "purpose": "⚠️ Rising Crisis & The Logical Dust Trick",
    "cameraAction": "Fox pushes his snout right into the hollow opening, sniffing hungrily. Rabbit spots fine dry sand and dust on the ground. Rabbit winks, digs his powerful hind legs in, and KICKS a massive blinding dust cloud straight into the fox's open eyes and nose!",
    "visualPrompt": "3D Pixar Disney style, medium dynamic action shot, clever brown bunny inside tree hollow kicking his powerful hind legs, blasting a thick dramatic cloud of fine golden sand and dry dirt directly into the face and eyes of the sneaking red fox, fox squinting and coughing in shock, dynamic motion blur, 8k render --ar 9:16",
    "teluguVO": "\"నక్క తొర్రలోకి ముఖం పెట్టి చూసింది! కానీ కుందేలు ఏమాత్రం భయపడలేదు! బుర్ర ఉపయోగించి తన వెనుక కాళ్లతో నేల మీదున్న దుమ్ము, ఇసుకను నక్క కళ్లల్లోకి గట్టిగా తన్నింది!\"",
    "englishSub": "\"Fox stuck his snout into the hole! But Bunny stayed calm... using his powerful hind legs, he kicked a thick cloud of dust and sand straight into the fox's eyes!\"",
    "sfx": "0:11s Sniffing Sound • 0:13s Cartoon Lightbulb PING • 0:16s Powerful Sand Whoosh Blast • 0:18s Fox Shocked Yelp"
}

ep1['clips'][2] = {
    "clipNumber": 3,
    "timeRange": "00:20 – 00:30 (10 Seconds)",
    "purpose": "💡 Comic Fall (Trip on Root) + Moral + NEXT EPISODE TEASER + Follow CTA",
    "cameraAction": "20–25s: Blinded and rubbing his eyes, the sneezing fox stumbles backward blindly, catches his back foot on a twisted mossy tree root, flips upside down, and crashes face-first SPLAT into a squishy mud puddle! Rabbit skips out safely waving. 25–26.5s: Moral card. 26.5–30s: CUT TO TEASER FRAME of Episode 2 (Crocodile eyeing Monkey on tree branch) + Bouncing Follow Button!",
    "visualPrompt": "3D Pixar Disney style, split sequence: comical blinded red fox tripping over a gnarled wooden tree root, flipping and landing face-first with a huge splash in a muddy brown puddle, silly stars circling his head, cute happy bunny skipping past him waving. Then cuts to teaser frame of huge green crocodile in sparkling blue river smiling slyly at a cute little monkey on a branch, 8k --ar 9:16",
    "teluguVO": "\"కళ్లు కనిపించక తుమ్ముతూ పరుగెత్తిన నక్క... చెట్టు వేరు తగిలి ధబ్ మని బురదలో పడిపోయింది! కుందేలు తుర్రుమంది! ఉపాయం ఉంటే అపాయం దాటొచ్చు! మరి రేపటి కథలో... మొసలి నోటి నుండి తెలివైన కోతి ఎలా తప్పించుకుంది? రేపటి ఎపిసోడ్ కోసం ఇప్పుడే FOLLOW చేయండి!\"",
    "englishSub": "\"Blinded and sneezing, the fox ran blindly, tripped on a tree root, and SPLAT crashed into the mud! Bunny skipped away free! Brain beats brawn! But tomorrow in Ep 2: How does a clever monkey escape a crocodile?! TAP FOLLOW NOW!\"",
    "sfx": "0:21s Cartoon Cough-Sneeze • 0:22s Tree Root Trip Thud • 0:23s Giant Mud Splash Splat • 0:25s Triumphant Fanfare • 0:29s High Crystal Bell Chime"
}

with open(r'C:\Users\Suresh\.gemini\antigravity-ide\scratch\panchatantra-dashboard\src\episodes.js', 'w', encoding='utf-8') as f:
    f.write('export const episodes = ' + json.dumps(eps, ensure_ascii=False, indent=2) + ';\n')

print('SUCCESS: Updated Episode 01 in episodes.js with 100% airtight cause-and-effect logic!')
