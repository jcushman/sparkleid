import base64
import random
import unicodedata

chars= """˼˻˺˹˸˴˳˰˯ˬ˞˜˛˚˙˘˖˗˕˔˓˒ˑːˏˎˍˌˋˊˉˈˇˆˁˀʽʼʿʾʻʺʹ`"'º¸·¦¯´¨΅΄ͺ͵‗‘’‚‛“”„‟†‡•‣․‥…‧‵‶‷‸‹›⏐⏑⏒⏓⎸⎹⎺⎻⎼⎽⎮⍿⍽⍸⍳⍪⍘⌜⌝⌞⌟⌠⌡⌔⌈⌉⌊⌋⌌⌍⌎⌏⌐⌑⌇⌁⦁⦂⦙⦚⋄⋅∼∽∾∿≀≁∴∵∶∷∘∙◦▴▪▫╴╵╶╷╸╹╺╻╮╯╰╎┙┚┕┖┑┒┍┎⬨⬩⬪⬫⬝⬞⠁❲❳❬❭❘✧⚬⚘⚕⚊꠶꠷꠨꠩╭⑀⎾⎿⌯℩᭼᎒᎓᎐༚༛༜༝༞༟￩￪￫￬⫶⨼⨽⨾⟊⎯⋮∗｡､꧇⸰⸒⸀⸁⸆⸇⸈⸋⳾⳿⁝⁚⁎⁃‾᱾᭜᭝᠊᠂᠃᠄᛫᛬᛭፣፤፥፦፧፡჻࿒་༌૰॰߸߹՚՛՜՝՞՟։"""

# check width
last_c = " "
for c in chars:
    print(last_c + c, '***')
    last_c = c

# remove combining and bidirectional chars
chars = [c for c in chars if unicodedata.combining(c) == 0 and unicodedata.bidirectional(c) in ['L', 'ON']]

# remove duplicates
chars = "".join(list(dict.fromkeys(chars)))

# show remaining, with length
print(len(chars), chars)

# show examples
to_int = {c: i for i, c in enumerate(chars)}
for i in range(10):
    s = "".join(random.sample(chars, 32))
    b64 = base64.b64encode(bytes(to_int[c] for c in s)).decode('utf8')
    print(f"{b64} -> {s}")

# useful for adding new candidates
c2 = """"""
print("candidates", "".join(c for c in c2 if ord(c)>127))
