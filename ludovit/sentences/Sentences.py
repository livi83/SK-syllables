import re
class Sentences:
    """
        Separating text to sentences
    """

    def get_sentences(self, text: str) -> list[str]:
        text = text.split()
        abrev = ["a.s.","admin.", "afr.", "a i.", "al.", "amer.", "anat.", "angl.", "anorg.", "ap., a pod.", "arab.", "arch.", "archeol.", "archit.", "astron.", "atď.", "aut.", "ázij.", "ban.", "bezpredm.", "bibl.", "biol.", "bot.", "bud.", "burž.", "býv.", "cirk.", "cit.", "cukrár.", "cukrovar.", "č.", "čast.", "čes.", "čísl.", "číslov.", "čs.", "D, dat.", "defekt.", "det.", "dipl.", "div.", "distrib.", "dok.", "dopr.", "dram.", "druh.", "duš.", "dvojčl.", "ekol.", "ekon.", "elektr.", "elektrotech.", "energet.", "est.", "eur.", "ev.", "expr.", "fam.", "farm.", "feud.", "filat.", "film.", "filol.", "filoz.", "fin.", "fín.", "fon.", "fot.", "franc.", "fraz.", "fyz.", "fyziol.", "G, gen.", "garb.", "genet.", "geod.", "geogr.", "geol.", "geom.", "graf.", "gréc.", "gréckokat.", "gram.", "hebr.", "hist.", "hl., hlav.", "hod.", "hosp.", "hovor.", "hromad.", "hrub.", "hud.", "hut.", "hyd.", "hypok.", "chem.", "chorv.", "I, inštr.", "inf.", "inform.", "ind.", "iron.", "jap.", "jedn., j. č.", "juhoamer.", "juhových.", "juhozáp.", "juž.", "kapit.", "kart.", "kat.", "ker.", "knih.", "kniž.", "kozmet.", "kraj.", "krajč.", "kresť.", "kt.", "kuch.", "kult.", "L, lok.", "lat.", "latinskoamer.", "lek.", "les.", "let.", "lingv.", "lit.", "log.", "ľud.", "m.", "maď.", "mal.", "mat.", "medzinár.", "mech.", "meteor.", "metr.", "mil.", "min., min. č.", "miner.", "mn., mn. č.", "motor.", "muž.", "mytol.", "N, nom.", "náb.", "napr.", "nár.", "nás.", "naznač.", "nedok.", "nem.", "neodb.", "neos.", "neskl.", "nespis.", "nespráv.", "neurč.", "neved.", "neživ.", "niekt.", "niž. hovor.", "n.l.", "obch.", "obuv.", "obyč.", "odb.", "odkaz.", "op.", "opak.", "opt.", "opyt.", "org.", "os.", "oslab.", "osob.", "ovoc.", "označ.", "oznam.", "oznam. tech.", "ped.", "pejor.", "peňaž.", "pís.", "pl.", "plat.", "po Kr.", "pod.", "podm.", "podraď.", "podst.", "podst. m.", "poet.", "poľ.", "polit.", "politol.", "poľnohosp.", "poľov.", "polygr.", "pomn.", "porov.", "pošt.", "potrav.", "použ.", "pôdohosp.", "pôv.", "prac.", "práv.", "pred Kr.", "predl.", "pren.", "príč.", "príd.", "príp.", "prír.", "priraď.", "prísl.", "príslov.", "privl.", "psych.", "publ.", "r.", "rad.", "rádiotech.", "reč.", "resp.", "rím.", "rob.", "róm.", "rozhlas.", "rozk.", "rozlič.", "rozpráv.", "rumun.", "rus.", "ryb.", "s.", "sev.", "severoamer.", "skr.", "sg.", "skup.", "slang.", "sloven.", "soc.", "sociol.", "soch.", "sov.", "spis.", "spoj.", "spoloč.", "spôs.", "správ.", "srb.", "st.", "star.", "starogréc.", "starorím.", "stav.", "stol.", "stor.", "stred., str.", "stredoamer.", "stredoškol.", "stroj.", "subšt.", "súvzť.", "svet.", "sv.", "šach.", "škol.", "špan.", "šport.", "št.", "štud.", "štyl.", "švéd.", "tal.", "tech.", "tel.", "teles.", "telef.", "telev.", "text.", "t. j.", "tur.", "turist.", "typ.", "tzv.", "účt.", "ukaz.", "umel.", "urč.", "úr.", "V, vok.", "včel.", "ved.", "vedľ.", "ver.", "veter.", "vin.", "vodohosp.", "voj.", "v spoj.", "všeob.", "vulg.", "vých.", "vyj.", "vymedz.", "výr.", "vys.", "výsl.", "vysokoškol.", "výtvar.", "význ.", "vzťaž.", "záhr.", "zákl.", "zám.", "záp.", "západoeur.", "zápor.", "zastar.", "zastaráv.", "zdrav.", "zdrob.", "zjemn.", "zlat.", "zlom.", "zn.", "zool.", "zried.", "zv.", "zvel.", "zvol.", "zvrat.", "ž.", "žart.", "žel.", "žen.", "žid.", "živ.", "dr.", "phd.", "ph.d.", "prof.", "csc.", "mgr.", "bc.", "doc."]
        punct = ['.','?','!']
        sentences = []
        str = ""
        
        for t in text:
            word = t.lower()
            str+=word+" "
            if word[-1] in punct and word not in abrev:
                if not word[len(word)-2].isnumeric():
                    print(word)
                    sentences.append(str.rstrip())
                    str = ""
        return sentences