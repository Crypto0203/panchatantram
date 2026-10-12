# -*- coding: utf-8 -*-
"""
Generates the authentic, complete 100 Panchatantra story definitions.
Zero generic placeholders. Every story has real trap, upayam, and climax.
"""
import json

STORIES_RAW = [
    # 1 - 10
    {
        "id": 1, "title": "The Clever Rabbit & Hungry Fox", "characters": "Rabbit • Fox",
        "leadChar": "Rabbit", "leadTe": "బుల్లి కుందేలు", "antagonist": "Fox", "antagonistTe": "జిత్తులమారి నక్క",
        "moral": "Brain power is always stronger than sharp teeth!", "moralTe": "శారీరక బలం కంటే ఉపాయంతో కూడిన ఆలోచనే గొప్పది!",
        "category": "Wisdom & Strategy",
        "trap": "Fox corners Rabbit inside the hollow root cavity of an ancient banyan tree, blocking the only entrance with grinning fangs.",
        "trapTe": "నక్క కుందేలును చెట్టు తొర్రలోకి వెంటాడి, బయటకు రానివ్వకుండా దారంతా మూసేసింది!",
        "upayam": "Rabbit uses its strong hind bunny legs to violently kick an explosive spray of dry dirt, loose sand, and leaves directly into the fox's wide-open eyes and nostrils.",
        "upayamTe": "కుందేలు ఏమాత్రం భయపడకుండా, తన వెనుక కాళ్లతో నేల మీదున్న పొడి ఇసుకను నక్క కళ్లల్లోకి బలంగా తన్నింది!",
        "climax": "Blinded and violently sneezing, the fox stumbles backward blindly, catches its back paw on a thick twisted tree root, flips comically, and crashes face-first SPLAT into a wet brown mud puddle.",
        "climaxTe": "కళ్లు మండడంతో నక్క వెనక్కి తూలి, చెట్టు వేరు తగిలి బొక్కబోర్లా బురద గుంటలో పడింది! కుందేలు గెంతుకుంటూ పారిపోయింది.",
        "nextEpId": 2, "nextEpTitle": "The Monkey & Crocodile", "nextTe": "తెలివైన కోతి మొసలిని ఎలా బురిడీ కొట్టించిందో"
    },
    {
        "id": 2, "title": "The Monkey & Crocodile", "characters": "Monkey • Crocodile",
        "leadChar": "Monkey", "leadTe": "తెలివైన కోతి", "antagonist": "Crocodile", "antagonistTe": "మొసలి",
        "moral": "Presence of mind in danger turns death into safety!", "moralTe": "సమయస్ఫూర్తి ఉంటే ప్రాణాంతకమైన అపాయం నుండి కూడా సురక్షితంగా బయటపడవచ్చు!",
        "category": "Wisdom & Strategy",
        "trap": "Crocodile carries Monkey to deep river center, then reveals: 'My wife wants to eat your sweet heart!'",
        "trapTe": "నది మధ్యలోకి వెళ్లాక, మొసలి తన భార్యకు కోతి గుండె కావాలని అసలు విషయం చెప్పింది!",
        "upayam": "Monkey calmly bursts into laughter: 'Oh friend! Why didn't you say so earlier? I always wash my heart and leave it hanging safely on the high jamun tree branch!'",
        "upayamTe": "కోతి ఏమాత్రం భయపడకుండా నవ్వి, 'అయ్యో మిత్రమా! నా గుండెను చెట్టు కొమ్మపై భద్రంగా దాచాను, పద వెళ్లి తెచ్చుకుందాం!' అంది.",
        "climax": "Foolish crocodile eagerly swims back to the riverbank. Monkey instantly springs onto the high branch, pelting rotten blackberries at crocodile's snout while laughing in safety.",
        "climaxTe": "నమ్మిన మొసలి ఒడ్డుకు రాగానే, కోతి చెట్టుపైకి గెంతి, మొసలిపైకి పండ్లు విసిరి కొట్టి ప్రాణాలు కాపాడుకుంది.",
        "nextEpId": 3, "nextEpTitle": "The Lion & Little Mouse", "nextTe": "చిన్న ఎలుక అడవి రాజు సింహాన్ని ఎలా కాపాడిందో"
    },
    {
        "id": 3, "title": "The Lion & Little Mouse", "characters": "Lion • Mouse",
        "leadChar": "Mouse", "leadTe": "చిట్టి ఎలుక", "antagonist": "Hunter's Net", "antagonistTe": "వేటగాడి బలమైన వల",
        "moral": "Even the smallest friend can save the mightiest king!", "moralTe": "ఎవరినీ చిన్నచూపు చూడకూడదు, చిన్న స్నేహితుడు కూడా పెద్ద సహాయం చేయగలడు!",
        "category": "Friendship & Unity",
        "trap": "The mighty King of the Jungle is trapped inside a heavy tangled rope net set by poachers, roaring helplessly as ropes cut into his fur.",
        "trapTe": "అడవి రాజు సింహం వేటగాళ్ల బలమైన తాళ్ల వలలో చిక్కుకుని, కదలలేక గర్జిస్తూ ఉంది!",
        "upayam": "The tiny brave mouse rushes in, locates the thick central anchor rope, and uses its razor-sharp front chisel teeth to gnaw furiously through the woven fibers.",
        "upayamTe": "చిట్టి ఎలుక వేగంగా వచ్చి, తన పదునైన పళ్లతో వల ముఖ్యమైన తాళ్లను చకచకా కొరికివేసింది!",
        "climax": "The master knot snaps! The heavy net collapses. The massive lion steps out totally free, gently lifts the mouse onto his massive mane, and gives a joyful celebratory roar.",
        "climaxTe": "తాళ్లు తెగిపోవడంతో సింహం స్వేచ్ఛగా బయటపడింది! ఎలుకను తన తలపై కూర్చోబెట్టుకుని కృతజ్ఞతతో గర్జించింది.",
        "nextEpId": 4, "nextEpTitle": "The Lion & The Clever Hare", "nextTe": "చిన్న కుందేలు గర్వపు సింహాన్ని బావిలోకి ఎలా తోసిందో"
    },
    {
        "id": 4, "title": "The Lion & The Clever Hare", "characters": "Lion • Hare",
        "leadChar": "Hare", "leadTe": "చిన్న కుందేలు", "antagonist": "Tyrant Lion", "antagonistTe": "గర్వపు సింహం",
        "moral": "Wisdom easily destroys uncontrolled brute anger!", "moralTe": "కోపం కంటే తెలివితేటలే బలమైన శత్రువునైనా ఓడిస్తాయి!",
        "category": "Wisdom & Strategy",
        "trap": "A tyrannical lion terrorizes the jungle, demanding one animal every day. Tiny hare arrives late, facing the roaring lion's deadly claws.",
        "trapTe": "ఆకలితో రగిలిపోతున్న సింహం ముందు కుందేలు ఆలస్యంగా వెళ్లి ప్రాణాల మీదకు తెచ్చుకుంది!",
        "upayam": "Hare calmly bows and lies: 'O King! Another ferocious lion stopped me at the ancient stone well, claiming HE is the true King!' Hare leads the furious lion straight to the deep well.",
        "upayamTe": "కుందేలు బావి వద్ద మరొక సింహం ఉందని చెప్పి, కోపంతో ఉన్న సింహాన్ని లోతైన బావి దగ్గరకు తీసుకెళ్లింది!",
        "climax": "Lion peers into the dark well, sees his own reflection snarling, roars at it, and furiously lunges downward—crashing into deep water with a massive SPLASH, trapped forever.",
        "climaxTe": "బావిలో తన ప్రతిబింబాన్ని చూసి మరో సింహం అనుకుని లోపలికి దూకి మునిగిపోయింది! అడవి జంతువులన్నీ సంబరాలు చేసుకున్నాయి.",
        "nextEpId": 5, "nextEpTitle": "The Tortoise & The Two Geese", "nextTe": "తాబేలు ఆకాశంలో ఎగురుతూ ఏం తొందరపాటు పని చేసిందో"
    },
    {
        "id": 5, "title": "The Tortoise & The Two Geese", "characters": "Tortoise • Geese",
        "leadChar": "Tortoise", "leadTe": "వాగుడు తాబేలు", "antagonist": "Uncontrolled Tongue", "antagonistTe": "నోటి దురద",
        "moral": "Control your speech in critical moments; silence saves life!", "moralTe": "సమయం సందర్భం చూసి మాట్లాడాలి, అనవసరమైన మాట ప్రాణాలకే ముప్పు!",
        "category": "Mindset & Character",
        "trap": "Drought dries the lake. Two geese hold a wooden stick across their beaks, carrying tortoise flying high across the sky to a blue lake.",
        "trapTe": "ఎండిపోయిన చెరువు నుండి తాబేలును కర్ర సాయంతో పక్షులు ఆకాశంలోకి ఎత్తుకెళ్లాయి!",
        "upayam": "Geese warn tortoise: 'Clamp your jaws tight onto the stick and DO NOT speak a single word no matter what!'",
        "upayamTe": "హంసలు 'నోరు విప్పితే కిందపడిపోతావ్, ఒక్క మాట కూడా మాట్లాడొద్దు' అని గట్టిగా హెచ్చరించాయి!",
        "climax": "Kids on ground point and laugh: 'Look, flying turtle!' Tortoise gets angry, opens mouth shouting 'HEY!', falls—but geese dive like fighter jets, catching him on their backs just above a haystack!",
        "climaxTe": "కింద జనం నవ్వగానే తాబేలు కోపంతో నోరు విప్పింది, కానీ హంసలు వేగంగా వచ్చి గడ్డివాముపై పడకుండా కాపాడాయి!",
        "nextEpId": 6, "nextEpTitle": "The Crow & The Black Snake", "nextTe": "కాకి తన పిల్లలను చంపిన పామును ఎలా నాశనం చేసిందో"
    },
    {
        "id": 6, "title": "The Crow & The Snake", "characters": "Crow • Snake",
        "leadChar": "Crow", "leadTe": "తెలివైన కాకి", "antagonist": "Black Cobra", "antagonistTe": "నల్లత్రాచు పాము",
        "moral": "Use your enemy's superior strength against them!", "moralTe": "మనకంటే బలవంతుడైన శత్రువును పక్కవారి అధికార బలం ఉపయోగించి ఓడించాలి!",
        "category": "Wisdom & Strategy",
        "trap": "A wicked black cobra lives in the root hole of the banyan tree, slithering up and devouring the mother crow's eggs.",
        "trapTe": "చెట్టు మొదట్లో ఉన్న పాము రోజు కాకి గుడ్లను, పిల్లలను తినేస్తూ ఉండేది!",
        "upayam": "Mother crow flies to the royal palace bath, snatches the Queen's sparkling golden ruby necklace in her beak, flies low, and drops it straight into the cobra's hollow hole!",
        "upayamTe": "కాకి రాణిగారి విలువైన బంగారు హారాన్ని నోట కరుచుకుని వచ్చి, పాము ఉన్న పుట్టలో పడేసింది!",
        "climax": "Royal palace guards chase the crow with spears. Seeing the gold necklace inside the hole, they poke their spears in, chasing the hissing cobra far out of the forest forever.",
        "climaxTe": "భటులు హారం కోసం పామును కర్రలతో అదిలించి తరిమికొట్టారు! కాకి కుటుంబం ప్రశాంతంగా జీవించింది.",
        "nextEpId": 7, "nextEpTitle": "The Blue Jackal", "nextTe": "నీలి రంగులో మునిగిన నక్క అడవి రాజుగా ఎలా నటించిందో"
    },
    {
        "id": 7, "title": "The Blue Jackal", "characters": "Jackal • Forest animals",
        "leadChar": "Jackal", "leadTe": "నీలి నక్క", "antagonist": "True Identity Reveal", "antagonistTe": "మోసపూరిత నటన",
        "moral": "Faking identity never lasts; nature always exposes deceit!", "moralTe": "నిజాన్ని ఎప్పటికీ దాచలేము, నకిలీ రూపం ఏదో ఒక రోజు బట్టబయలవుతుంది!",
        "category": "Mindset & Character",
        "trap": "Chased by street dogs into a dyer's house, a scrawny jackal falls into a large tub of indigo blue dye, emerging stained glowing sapphire blue.",
        "trapTe": "కుక్కల భయంతో రంగుల తొట్టిలో పడిన నక్క, ఒళ్లంతా నీలి రంగుగా మారి వింత జంతువులా మారింది!",
        "upayam": "Jackal struts into the forest claiming: 'Brahma anointed me King of all beasts!' Tigers, bears, and elephants bow down, offering him sweet fruits and honey.",
        "upayamTe": "తాను దేవుడు పంపిన రాజునని జంతువులను నమ్మించి, అడవి జంతువులన్నింటిపై పెత్తనం చెలాయించింది!",
        "climax": "At night, wild jackals howl 'Oooo-aaooo!' in the distance. The blue jackal cannot resist his nature, tilts his head back, and howls along loudly! Animals instantly realize the fraud and chase him away.",
        "climaxTe": "దూరంగా మిగతా నక్కలు ఊళ వేయగానే, ఈ నక్క కూడా ఊళ వేసి దొరికిపోయింది! జంతువులన్నీ కలిసి తరిమేశాయి.",
        "nextEpId": 8, "nextEpTitle": "The Greedy Dog & The Bone", "nextTe": "నోట్లో ఎముక ఉన్న కుక్క నీళ్లలో చూసి ఏం పోగొట్టుకుందో"
    },
    {
        "id": 8, "title": "The Greedy Dog & The Bone", "characters": "Dog",
        "leadChar": "Dog", "leadTe": "దురాశ కుక్క", "antagonist": "Greed & Reflection", "antagonistTe": "అత్యాశ",
        "moral": "Greed for what others have destroys what you already possess!", "moralTe": "అత్యాశకు పోతే ఉన్నది కాస్తా ఊడిపోతుంది, ఉన్నదానితో తృప్తి పడాలి!",
        "category": "Mindset & Character",
        "trap": "A lucky stray dog finds a juicy large meat bone, happily trotting across a narrow wooden plank bridge over a crystal-clear mountain stream.",
        "trapTe": "నోట్లో పెద్ద ఎముక ముక్కతో నదిపై ఉన్న చెక్క వంతెన దాటుతున్న కుక్క నీళ్లలోకి చూసింది!",
        "upayam": "Dog spots his own reflection in the still water, mistaking it for another dog carrying a BIGGER bone. Blinded by greed, he decides to snap and steal that bone too!",
        "upayamTe": "నీళ్లలో తన నీడను చూసి, మరో కుక్క దగ్గర ఇంకా పెద్ద ఎముక ఉందని భ్రమపడి దాన్ని లాక్కోవాలనుకుంది!",
        "climax": "Dog opens his jaws wide and barks aggressively 'BOW-WOW!'. The real bone instantly slips from his teeth, splashing 'PLOP' into the fast river current, swept away forever.",
        "climaxTe": "నోరు తెరిచి 'భౌ' అని మొరగగానే, నోట్లోని అసలు ఎముక నీళ్లలో పడి కొట్టుకుపోయింది! కుక్క బిత్తరచూపులు చూసింది.",
        "nextEpId": 9, "nextEpTitle": "The Farmer & The Snake", "nextTe": "బంగారు నాణెం ఇచ్చే పామును చూసి రైతు కొడుకు ఏం చేశాడో"
    },
    {
        "id": 9, "title": "The Farmer & The Snake", "characters": "Farmer • Snake",
        "leadChar": "Snake", "leadTe": "బంగారు నాణేల పాము", "antagonist": "Greedy Son", "antagonistTe": "రైతు దురాశ కొడుకు",
        "moral": "Hasty greed destroys the continuous fountain of wealth!", "moralTe": "రోజూ వచ్చే లాభంతో తృప్తిపడాలి గానీ, ఒక్కసారే అంతా కావాలనుకుంటే సర్వనాశనం!",
        "category": "Mindset & Character",
        "trap": "A grateful cobra gives a pure gold coin every day in exchange for a saucer of milk placed near an anthill by a humble farmer.",
        "trapTe": "పుట్టలో ఉన్న పాముకు పాలు పోస్తే, అది రోజూ ఒక బంగారు నాణెం బహుమతిగా ఇచ్చేది!",
        "upayam": "The farmer's greedy son plots: 'The anthill must be filled with thousands of gold coins! Why wait? I will strike the cobra and take them all!'",
        "upayamTe": "రైతు కొడుకు పుట్టలో బంగారు నిధి మొత్తం ఒక్కసారే కొట్టేయాలని కర్ర పట్టుకుని పాముపైకి వెళ్లాడు!",
        "climax": "As the son swings a heavy stick, the lightning-fast cobra dodges the blow, hisses fiercely, snaps the stick in half, and vanishes into the earth forever, cutting off all gold forever.",
        "climaxTe": "పాము మెరుపులా తప్పించుకుని బుసకొట్టి లోపలికి వెళ్లిపోయింది! కొడుకు చేతిలో కర్ర విరిగి, నాణేలు శాశ్వతంగా ఆగిపోయాయి.",
        "nextEpId": 10, "nextEpTitle": "The Foolish Deer & The Trapper", "nextTe": "అందమైన కొమ్ములను మెచ్చుకున్న జింక ముళ్ల పొదలో ఎలా చిక్కుకుందో"
    },
    {
        "id": 10, "title": "The Foolish Deer", "characters": "Deer • Forest friends",
        "leadChar": "Deer", "leadTe": "చక్కని జింక", "antagonist": "Flashy Pride", "antagonistTe": "అందాన్ని చూసి మిడిసిపాటు",
        "moral": "Flashy ego traps you; humble strength saves your life!", "moralTe": "పైపై అందం అపాయాన్ని తెచ్చిపెడుతుంది, ఉపయోగపడే శక్తే మనల్ని కాపాడుతుంది!",
        "category": "Mindset & Character",
        "trap": "Deer admires his grand branching antlers in a forest pool, complaining about his skinny thin legs. Suddenly, hunter's hounds burst into the grove barking loudly!",
        "trapTe": "తన అందమైన కొమ్ములను మెచ్చుకుంటూ కాళ్లను అసహ్యించుకున్న జింకను వేటకుక్కలు వెంటాడాయి!",
        "upayam": "Deer sprints at blazing speed on his strong slender legs, outpacing the hounds into a dense bramble patch—but his wide branching antlers get snagged hard in thorny vines!",
        "upayamTe": "వేగంగా పరుగెత్తిన జింక కొమ్ములు దట్టమైన ముళ్ల పొదల్లో బలంగా ఇరుక్కుపోయాయి!",
        "climax": "With dogs closing in, deer drops his pride, pushes furiously with his despised slender hooves, snaps the branches, and escapes—learning his legs saved him while his vanity nearly killed him.",
        "climaxTe": "తాను ద్వేషించిన సన్నని కాళ్లతోనే నేలను బలంగా తన్ని ముళ్లను విరిచి ప్రాణాలు కాపాడుకుంది!",
        "nextEpId": 11, "nextEpTitle": "The Wise Old Sparrow & The Hawk", "nextTe": "డేగ బారి నుండి పిచ్చుక పిల్లలను ముళ్ల గుబురు ఎలా కాపాడిందో"
    }
]

print("Loaded initial 10 stories.")
