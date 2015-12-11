import csv, re

origin = "MASTER_round2_titles_w-better-separators_v2.csv"
destination = "final_titles_separated.csv"
writer = csv.writer(open(destination, "wb"))
masterPattern = "(\(US.*|\(U.S.*|\(Fran.*|\(Turk.*|\(Denm.*" \
                "|\(Brazi.*|\(Ital.*|\(German.*|\(\ US.*|\(Japa.*" \
                "|\(Pola.*|\(East.*|\(Chin.*|\(Swed.*|\(Swi.*|\(Russi.*" \
                "|\(FRA.*|\(gree.*|\(Venez.*|\(Viet.*|\(West G.*" \
                "|\(iran.*|\(india.*|\(South Af.*|\(Hong .*|\(Nether.*" \
                "|\(Belg.*|\(Morocc.*|\(Brit.*|\(Egypt.*|\(UK.*|\(U.K.*" \
                "|\(Great Br.*|\(Argentin.*|\(Israel.*|\(Taiwan.*|\(Kazakh.*" \
                "|\(canad.*|\(austr.*|\(soviet.*|\(thai.*|\(ireland.*|\(mexic.*" \
                "|\(hungar.*|\(south kor.*|\(spain.*|\(indones.*|\(w. ger.*" \
                "|\(e. ger.*|\(czech.*|\(syria.*|\(yugosl.*|\(philippin.*" \
                "|\(spanish.*|\(Ecuad.*|\(Holla.*|\(romania.*|\(iceland.*" \
                "|\(malay.*|\(portug.*|\(french.*|\(danish.*|\(norw.*|\(bulgar.*" \
                "|\(chile.*|\(nigeria.*|\(nederland.*|\(the nether.*|\(united .*" \
                "|\(mali.*|\(w.ger.*|\(e.ger.*|\(finla.*|\(finni.*|\(bosnia.*" \
                "|\(costa r.*|\(tunisia.*|\(lao.*|\(filipino.*)"
patternComp = re.compile(masterPattern, re.IGNORECASE)

with open(origin, "rb") as full:
    for text in full:
        pattern = re.search(masterPattern,text, re.IGNORECASE)
        originalText = text.split("\t")
        if pattern:
            prod = pattern.group()
            prod2 = pattern.group()
            origLessProd = [prod for prod in originalText if not patternComp.search(prod)]
            #originalText.insert(0,prod)
            origLessProd.insert(0,prod2)
            writer.writerow(origLessProd)
            print(origLessProd)
        else:
            originalText.insert(0,"")
            writer.writerow(originalText)
            print(originalText)