import urllib2
import json
import os

def lambda_handler(event, context):
    if (event['session']['application']['applicationId'] !=
    os.environ['ALEXA_APPLICATION_ID']):
    raise ValueError("Invalid Application ID")

if event['session']['new']:
    on_session_started({'requestId': event['request']['requestId']}, event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
elif event['request']['type'] == "IntentRequest":
    return on_intent(event['request'], event['session'])
elif event['request']['type'] == "SessionEndedRequest":
    return on_session_ended(event['request'], event['session'])

def on_session_started(session_started_request, session):
    print "Starting new session."

    def on_launch(launch_request, session):
        return get_welcome_response()

    def on_intent(intent_request, session):
        intent = intent_request['intent']
        intent_name = intent_request['intent']['name']

        if intent_name == "GetArrivals":
            return get_arrivals(intent)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
    return handle_session_end_request()
else:
    raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    print "Ending session."

    def get_welcome_response():
        session_attributes = {}
        card_title = "TODO"
        speech_output = "Welcome to TODO.... " \
        "You can ask me for train times from any station."
        reprompt_text = "Please ask me for trains times from a station, " \
        "for example Embankment."
        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(
    card_title, speech_output, reprompt_text, should_end_session))

    def handle_session_end_request():
        card_title = "TODO"
        speech_output = "TODO message for when user ends session"
        should_end_session = True

        return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))


    def get_arrivals(intent):
        session_attributes = {}
        card_title = "TODO"
        speech_output = "I'm not sure which station you wanted train times for. " \
        "Please try again."
        reprompt_text = "I'm not sure which station you wanted train times for. " \
        "Try asking about Oxford Circus or Embankment for example."
        should_end_session = False

        speech_output = "TODO"
        reprompt_text = ""

        return build_response(session_attributes, build_speechlet_response(
    card_title, speech_output, reprompt_text, should_end_session))

    def get_station_code(station_name):
        return {
    "acton town": "940GZZLUACT",
    "aldgate": "940GZZLUALD",
    "aldgate east": "940GZZLUADE",
    "alperton": "940GZZLUALP",
    "amersham": "940GZZLUAMS",
    "angel": "940GZZLUAGL",
    "archway": "940GZZLUACY",
    "arnos grove": "940GZZLUASG",
    "arsenal": "940GZZLUASL",
    "baker street": "940GZZLUBST",
    "balham": "940GZZLUBLM",
    "bank": "940GZZLUBNK",
    "barbican": "940GZZLUBBN",
    "barking": "940GZZLUBKG",
    "barkingside": "940GZZLUBKE",
    "barons court": "940GZZLUBSC",
    "bayswater": "940GZZLUBWT",
    "becontree": "940GZZLUBEC",
    "belsize park": "940GZZLUBZP",
    "bermondsey": "940GZZLUBMY",
    "bethnal green": "940GZZLUBLG",
    "blackfriars": "940GZZLUBKF",
    "blackhorse road": "940GZZLUBLR",
    "bond street": "940GZZLUBND",
    "borough": "940GZZLUBOR",
    "boston manor": "940GZZLUBOS",
    "bounds green": "940GZZLUBDS",
    "bow road": "940GZZLUBWR",
    "brent cross": "940GZZLUBTX",
    "brixton": "940GZZLUBXN",
    "bromley-by-bow": "940GZZLUBBB",
    "buckhurst hill": "940GZZLUBKH",
    "burnt oak": "940GZZLUBTK",
    "caledonian road": "940GZZLUCAR",
    "camden town": "940GZZLUCTN",
    "canada water": "940GZZLUCWR",
    "canary wharf": "940GZZLUCYF",
    "canning town": "940GZZLUCGT",
    "cannon street": "940GZZLUCST",
    "canons park": "940GZZLUCPK",
    "chalfont and latimer": "940GZZLUCAL",
    "chalk farm": "940GZZLUCFM",
    "chancery lane": "940GZZLUCHL",
    "charing cross": "940GZZLUCHX",
    "chesham": "940GZZLUCSM",
    "chigwell": "940GZZLUCWL",
    "chiswick park": "940GZZLUCWP",
    "chorleywood": "940GZZLUCYD",
    "clapham common": "940GZZLUCPC",
    "clapham north": "940GZZLUCPN",
    "clapham south": "940GZZLUCPS",
    "cockfosters": "940GZZLUCKS",
    "colindale": "940GZZLUCND",
    "colliers wood": "940GZZLUCSD",
    "covent garden": "940GZZLUCGN",
    "croxley": "940GZZLUCXY",
    "dagenham east": "940GZZLUDGE",
    "dagenham heathway": "940GZZLUDGY",
    "debden": "940GZZLUDBN",
    "dollis hill": "940GZZLUDOH",
    "ealing broadway": "940GZZLUEBY",
    "ealing common": "940GZZLUECM",
    "earl's court": "940GZZLUECT",
    "east acton": "940GZZLUEAN",
    "east finchley": "940GZZLUEFY",
    "east ham": "940GZZLUEHM",
    "east putney": "940GZZLUEPY",
    "eastcote": "940GZZLUEAE",
    "edgware": "940GZZLUEGW",
    "edgware road (bakerloo)": "940GZZLUERB",
    "edgware road (circle line)": "940GZZLUERC",
    "elephant & castle": "940GZZLUEAC",
    "elm park": "940GZZLUEPK",
    "embankment": "940GZZLUEMB",
    "epping": "940GZZLUEPG",
    "euston": "940GZZLUEUS",
    "euston square": "940GZZLUESQ",
    "fairlop": "940GZZLUFLP",
    "farringdon": "940GZZLUFCN",
    "finchley central": "940GZZLUFYC",
    "finchley road": "940GZZLUFYR",
    "finsbury park": "940GZZLUFPK",
    "fulham broadway": "940GZZLUFBY",
    "gants hill": "940GZZLUGTH",
    "gloucester road": "940GZZLUGTR",
    "golders green": "940GZZLUGGN",
    "goldhawk road": "940GZZLUGHK",
    "goodge street": "940GZZLUGDG",
    "grange hill": "940GZZLUGGH",
    "great portland street": "940GZZLUGPS",
    "greenford": "940GZZLUGFD",
    "green park": "940GZZLUGPK",
    "gunnersbury": "940GZZLUGBY",
    "hainault": "940GZZLUHLT",
    "hammersmith (district and piccadilly line)": "940GZZLUHSD",
    "hammersmith (hammersmith and city line)": "940GZZLUHSC",
    "hampstead": "940GZZLUHTD",
    "hanger lane": "940GZZLUHGR",
    "harlesden": "940GZZLUHSN",
    "harrow & wealdstone": "940GZZLUHAW",
    "harrow-on-the-hill": "940GZZLUHOH",
    "hatton cross": "940GZZLUHNX",
    "heathrow terminals 1-2-3 ": "940GZZLUHRC",
    "heathrow terminal 4": "940GZZLUHR4",
    "heathrow terminal 5": "940GZZLUHR5",
    "hendon central": "940GZZLUHCL",
    "high barnet": "940GZZLUHBT",
    "highbury and islington": "940GZZLUHAI",
    "high street kensington": "940GZZLUHSK",
    "highgate": "940GZZLUHGT",
    "hillingdon": "940GZZLUHGD",
    "holborn": "940GZZLUHBN",
    "holland park": "940GZZLUHPK",
    "holloway road": "940GZZLUHWY",
    "hornchurch": "940GZZLUHCH",
    "hounslow central": "940GZZLUHWC",
    "hounslow east": "940GZZLUHWE",
    "hounslow west": "940GZZLUHWT",
    "hyde park corner": "940GZZLUHPC",
    "ickenham": "940GZZLUICK",
    "kennington": "940GZZLUKNG",
    "kensal green": "940GZZLUKSL",
    "kensington (olympia)": "940GZZLUKOY",
    "kentish town": "940GZZLUKSH",
    "kenton": "940GZZLUKEN",
    "kew gardens": "940GZZLUKWG",
    "kilburn": "940GZZLUKBN",
    "kilburn park": "940GZZLUKPK",
    "king's cross st. pancras": "940GZZLUKSX",
    "kingsbury": "940GZZLUKBY",
    "knightsbridge": "940GZZLUKNB",
    "ladbroke grove": "940GZZLULAD",
    "lambeth north": "940GZZLULBN",
    "lancaster gate": "940GZZLULGT",
    "latimer road": "940GZZLULRD",
    "leicester square": "940GZZLULSQ",
    "leyton": "940GZZLULYN",
    "leytonstone": "940GZZLULYS",
    "liverpool street": "940GZZLULVT",
    "london bridge": "940GZZLULNB",
    "loughton": "940GZZLULGN",
    "maida vale": "940GZZLUMVL",
    "manor house": "940GZZLUMRH",
    "mansion house": "940GZZLUMSH",
    "marble arch": "940GZZLUMBA",
    "marylebone": "940GZZLUMYB",
    "mile end": "940GZZLUMED",
    "mill hill east": "940GZZLUMHL",
    "monument": "940GZZLUMMT",
    "moor park": "940GZZLUMPK",
    "moorgate": "940GZZLUMGT",
    "morden": "940GZZLUMDN",
    "mornington crescent": "940GZZLUMTC",
    "neasden": "940GZZLUNDN",
    "newbury park": "940GZZLUNBP",
    "north acton": "940GZZLUNAN",
    "north ealing": "940GZZLUNEN",
    "north greenwich": "940GZZLUNGW",
    "north harrow": "940GZZLUNHA",
    "north wembley": "940GZZLUNWY",
    "northfields": "940GZZLUNFD",
    "northolt": "940GZZLUNHT",
    "northwick park": "940GZZLUNKP",
    "northwood": "940GZZLUNOW",
    "northwood hills": "940GZZLUNWH",
    "notting hill gate": "940GZZLUNHG",
    "oakwood": "940GZZLUOAK",
    "old street": "940GZZLUODS",
    "osterley": "940GZZLUOSY",
    "oval": "940GZZLUOVL",
    "oxford circus": "940GZZLUOXC",
    "paddington": "940GZZLUPAC",
    "paddington (hammersmith and city line)": "940GZZLUPAH",
    "park royal": "940GZZLUPKR",
    "parsons green": "940GZZLUPSG",
    "perivale": "940GZZLUPVL",
    "piccadilly circus": "940GZZLUPCC",
    "pimlico": "940GZZLUPCO",
    "pinner": "940GZZLUPNR",
    "plaistow": "940GZZLUPLW",
    "preston road": "940GZZLUPRD",
    "putney bridge": "940GZZLUPYB",
    "queen's park": "940GZZLUQPS",
    "queensbury": "940GZZLUQBY",
    "queensway": "940GZZLUQWY",
    "ravenscourt park": "940GZZLURVP",
    "rayners lane": "940GZZLURYL",
    "redbridge": "940GZZLURBG",
    "regent's park": "940GZZLURGP",
    "richmond": "940GZZLURMD",
    "rickmansworth": "940GZZLURKW",
    "roding valley": "940GZZLURVY",
    "royal oak": "940GZZLURYO",
    "ruislip": "940GZZLURSP",
    "ruislip gardens": "940GZZLURSG",
    "ruislip manor": "940GZZLURSM",
    "russell square": "940GZZLURSQ",
    "st. james's park": "940GZZLUSJP",
    "st. john's wood": "940GZZLUSJW",
    "st. paul's": "940GZZLUSPU",
    "seven sisters": "940GZZLUSVS",
    "shepherd's bush (central)": "940GZZLUSBC",
    "shepherd's bush market": "940GZZLUSBM",
    "sloane square": "940GZZLUSSQ",
    "snaresbrook": "940GZZLUSNB",
    "south ealing": "940GZZLUSEA",
    "south harrow": "940GZZLUSHH",
    "south kensington": "940GZZLUSKS",
    "south kenton": "940GZZLUSKT",
    "south ruislip": "940GZZLUSRP",
    "south wimbledon": "940GZZLUSWN",
    "south woodford": "940GZZLUSWF",
    "southfields": "940GZZLUSFS",
    "southgate": "940GZZLUSGT",
    "southwark": "940GZZLUSWK",
    "stamford brook": "940GZZLUSFB",
    "stanmore": "940GZZLUSTM",
    "stepney green": "940GZZLUSGN",
    "stockwell": "940GZZLUSKW",
    "stonebridge park": "940GZZLUSGP",
    "stratford": "940GZZLUSTD",
    "sudbury hill": "940GZZLUSUH",
    "sudbury town": "940GZZLUSUT",
    "swiss cottage": "940GZZLUSWC",
    "temple": "940GZZLUTMP",
    "theydon bois": "940GZZLUTHB",
    "tooting bec": "940GZZLUTBC",
    "tooting broadway": "940GZZLUTBY",
    "tottenham court road": "940GZZLUTCR",
    "tottenham hale": "940GZZLUTMH",
    "totteridge and whetstone": "940GZZLUTAW",
    "tower hill": "940GZZLUTWH",
    "tufnell park": "940GZZLUTFP",
    "turnham green": "940GZZLUTNG",
    "turnpike lane": "940GZZLUTPN",
    "upminster": "940GZZLUUPM",
    "upminster bridge": "940GZZLUUPB",
    "upney": "940GZZLUUPY",
    "upton park": "940GZZLUUPK",
    "uxbridge": "940GZZLUUXB",
    "vauxhall": "940GZZLUVXL",
    "victoria": "940GZZLUVIC",
    "walthamstow central": "940GZZLUWWL",
    "wanstead": "940GZZLUWSD",
    "warren street": "940GZZLUWRR",
    "warwick avenue": "940GZZLUWKA",
    "waterloo": "940GZZLUWLO",
    "watford": "940GZZLUWAF",
    "wembley central": "940GZZLUWYC",
    "wembley park": "940GZZLUWYP",
    "west acton": "940GZZLUWTA",
    "west brompton": "940GZZLUWBN",
    "west finchley": "940GZZLUWFN",
    "west ham": "940GZZLUWHM",
    "west hampstead": "940GZZLUWHP",
    "west harrow": "940GZZLUWHW",
    "west kensington": "940GZZLUWKN",
    "west ruislip": "940GZZLUWRP",
    "westbourne park": "940GZZLUWSP",
    "westminster": "940GZZLUWSM",
    "white city": "940GZZLUWCY",
    "whitechapel": "940GZZLUWPL",
    "willesden green": "940GZZLUWIG",
    "willesden junction": "940GZZLUWJN",
    "wimbledon": "940GZZLUWIM",
    "wimbledon park": "940GZZLUWIP",
    "wood green": "940GZZLUWOG",
    "wood lane": "940GZZLUWLA",
    "woodford": "940GZZLUWOF",
    "woodside park": "940GZZLUWOP"
    }.get(station_name, "unkn")

    def build_speechlet_response(title, output, reprompt_text, should_end_session):
        return {
    'outputSpeech': {
    'type': 'PlainText',
    'text': output
    },
    'card': {
    'type': 'Simple',
    'title': title,
    'content': output
    },
    'reprompt': {
    'outputSpeech': {
    'type': 'PlainText',
    'text': reprompt_text
    }
    },
    'shouldEndSession': should_end_session
    }

    def build_response(session_attributes, speechlet_response):
        return {
    'version': '1.0',
    'sessionAttributes': session_attributes,
    'response': speechlet_response
    }
