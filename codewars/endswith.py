#Task
'''
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
'''

def solution(text, ending):
    return ending in text[(len(text)-len(ending)):]


#Test Results:
'''
Fixed Tests
True Cases
 (6 of 6 Assertions)
False Cases
 (6 of 6 Assertions)
Completed in 0.17ms
Random tests
Testing for: text = "sjjxcyplbrqvvsm", ending = "rqvvsm" to return True
Testing for: text = "zazuzkazpfgtrwzrdpsrsb", ending = "fgtdwzwqpsrsn" to return False
Testing for: text = "gprmorspthifitnuunkpu", ending = "rrtthifionuunxpu" to return False
Testing for: text = "krxysetwhvtfjemmoczb", ending = "setwhbtfjepmoczb" to return False
Testing for: text = "twiaieieqtqpygieme", ending = "pygieme" to return True
Testing for: text = "pycstjfpdwrqse", ending = "stjfpdwrqse" to return True
Testing for: text = "ypxydvwoqhcyoumryqfsqjhx", ending = "qjhx" to return True
Testing for: text = "awyglyvicextamnrk", ending = "icextamnrk" to return True
Testing for: text = "xsfawalxgykhy", ending = "lxgykhy" to return True
Testing for: text = "rtosgaob", ending = "gaob" to return True
Testing for: text = "ennxjfejkgkesjlrozyrsqwsj", ending = "sqwsj" to return True
Testing for: text = "ixcetjfrzjkgge", ending = "frzjkgge" to return True
Testing for: text = "uvxdsmyawutcqjwz", ending = "jwz" to return True
Testing for: text = "bhlqfpcpsuq", ending = "psuq" to return True
Testing for: text = "tclmphfzhpsnscseopekbe", ending = "ekbe" to return True
Testing for: text = "qqgxybuzpm", ending = "uzpm" to return True
Testing for: text = "zpfjwhpdmpf", ending = "pf" to return True
Testing for: text = "yanjkyn", ending = "yn" to return True
Testing for: text = "qmuhhsjpmefx", ending = "fx" to return True
Testing for: text = "brvdpwdygwixjkxzqcb", ending = "gwixjkxzqcb" to return True
Testing for: text = "huxqw", ending = "uxqw" to return True
Testing for: text = "ghasdeldxl", ending = "deldxl" to return True
Testing for: text = "uwtfmxtsbkpnvbznuecc", ending = "mxtsbkpnvbznuecc" to return True
Testing for: text = "urrfeeqrxzz", ending = "feeqrxzz" to return True
Testing for: text = "scxizasgi", ending = "xizasgi" to return True
Testing for: text = "bykjlbcrnoineyqhde", ending = "lbcrnoineyqhde" to return True
Testing for: text = "bfiuqimbbyiyheziawmrqllko", ending = "iyheziawmrqllko" to return True
Testing for: text = "zgwxplwvhwiqz", ending = "hwiqz" to return True
Testing for: text = "qogxbjj", ending = "sxbjj" to return False
Testing for: text = "zwvljcnzinhxfnurhtgrmra", ending = "hxfnurhtgrmra" to return True
Testing for: text = "ftmvrhx", ending = "x" to return True
Testing for: text = "zjmxjgcebvavtbzcxnbjrqd", ending = "avtbzcxnbjrqd" to return True
Testing for: text = "uzgrlh", ending = "h" to return True
Testing for: text = "aiirizoaopdequtffb", ending = "equtffb" to return True
Testing for: text = "htzhruloplaewnwdjlhqccu", ending = "uloplaewnwdjlhqccu" to return True
Testing for: text = "uwezkpfsvt", ending = "fsvt" to return True
Testing for: text = "drphltqbwi", ending = "qbwi" to return True
Testing for: text = "kpwmhtuzozcxfg", ending = "uvozcxfg" to return False
Testing for: text = "zjkjdpflicfbajxossvmglwl", ending = "ossvmglwl" to return True
Testing for: text = "wzefyouqjotw", ending = "tw" to return True
Testing for: text = "kbjklxjjsnwudukhmftxpyjs", ending = "wudukhmftxpyjs" to return True
Testing for: text = "mmbamyikbu", ending = "bamyikbu" to return True
Testing for: text = "lqxkliezggijx", ending = "ggijx" to return True
Testing for: text = "btsqrwooogwdlne", ending = "lne" to return True
Testing for: text = "rbfbiyzeshjfawelfvppcf", ending = "yzeshjfawelfvppcf" to return True
Testing for: text = "ndmhpnoxblvsfekj", ending = "ekj" to return True
Testing for: text = "bkrajeahljnnbltltsixxf", ending = "tltsixfy" to return False
Testing for: text = "ovvgkmk", ending = "k" to return True
Testing for: text = "bsgyycfvyyysl", ending = "yycfvjyysl" to return False
Testing for: text = "fketzeknjgckvsjafrimsjhzv", ending = "afwimsvhzv" to return False
Testing for: text = "sflbzoxhbaufeqqea", ending = "hbaufeqqea" to return True
Testing for: text = "xqepjgyndqllyzngj", ending = "jgymdqllyznjj" to return False
Testing for: text = "fpjrrgas", ending = "s" to return True
Testing for: text = "chofomvfhpfhkmeeeixxoowl", ending = "fhkmeeeixxoowl" to return True
Testing for: text = "bbjvttukqsv", ending = "sv" to return True
Testing for: text = "ppaqjrxmend", ending = "mend" to return True
Testing for: text = "qmkavwtll", ending = "kavwtll" to return True
Testing for: text = "eurcbrzaxfgbqujxq", ending = "brzaxfgbqujxq" to return True
Testing for: text = "ldxgzdsgatdzebiahyqgevw", ending = "iahyqgevw" to return True
Testing for: text = "wewootzyqaxxdgbyms", ending = "qaxxdgbyms" to return True
Testing for: text = "jzsogpcygstgs", ending = "ogpcygstgs" to return True
Testing for: text = "dikbznhzwpwzrlexbutmbexqk", ending = "wzrlexbutmbexqk" to return True
Testing for: text = "cggxkjopqxrfoaxqva", ending = "foaxqva" to return True
Testing for: text = "ejwztfaugspo", ending = "faugspo" to return True
Testing for: text = "twwlkfnnckvzwt", ending = "wt" to return True
Testing for: text = "ojydqy", ending = "ydqy" to return True
Testing for: text = "yvqdxrzwexwedemjijmsrbtjq", ending = "rizmsrbtjq" to return False
Testing for: text = "glslljxmqhfl", ending = "jxmqhfi" to return False
Testing for: text = "uovedqqa", ending = "qqa" to return True
Testing for: text = "mbounk", ending = "nk" to return True
Testing for: text = "idhjytxxfzwzmtfugt", ending = "ugt" to return True
Testing for: text = "gzqkluy", ending = "kluy" to return True
Testing for: text = "epcqnmrsevamqzefx", ending = "mqzefc" to return False
Testing for: text = "evkleyxzscxgafmzg", ending = "gafdzg" to return False
Testing for: text = "jozqojxejfoeyauk", ending = "oeyauk" to return True
Testing for: text = "zatvtqyresjvzaxs", ending = "jvzaxs" to return True
Testing for: text = "ijbslflpfpaafuykx", ending = "pniaafutkx" to return False
Testing for: text = "htaljei", ending = "aljei" to return True
Testing for: text = "pjzsriznc", ending = "riznc" to return True
Testing for: text = "agjlkafio", ending = "kafio" to return True
Testing for: text = "fuidazqnuj", ending = "idazqnuj" to return True
Testing for: text = "jaqzehufqampmnhbfbxxibf", ending = "mpmnhbfpxxibf" to return False
Testing for: text = "wupgu", ending = "gu" to return True
Testing for: text = "eeszlqlqabfhdoxvkyghg", ending = "yghg" to return True
Testing for: text = "swdoraodznwdhvdzo", ending = "dzo" to return True
Testing for: text = "vfeagsjafppt", ending = "agsjafppt" to return True
Testing for: text = "inyopralf", ending = "pralf" to return True
Testing for: text = "pfjvydou", ending = "dou" to return True
Testing for: text = "oufeqpezgfj", ending = "vqpezgfj" to return False
Testing for: text = "uyljqq", ending = "qq" to return True
Testing for: text = "vogogneirawwnj", ending = "awwnj" to return True
Testing for: text = "bpkxtfjmwnboy", ending = "oy" to return True
Testing for: text = "dgpnuuu", ending = "uu" to return True
Testing for: text = "ecfjajrfpu", ending = "rfpu" to return True
Testing for: text = "zxikuzf", ending = "ikuzf" to return True
Testing for: text = "gblvmbrtqd", ending = "rtqd" to return True
Testing for: text = "wxdroab", ending = "roab" to return True
Testing for: text = "keoutjhghn", ending = "outjhghn" to return True
Testing for: text = "lbytrjuwuidjyjaymdcjcjjd", ending = "ymdcjcjjd" to return True
Testing for: text = "qfuypke", ending = "e" to return True
Completed in 7.65ms
You have passed all of the tests! :)
'''