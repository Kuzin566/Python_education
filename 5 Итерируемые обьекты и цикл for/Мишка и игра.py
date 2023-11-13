"""Мишка — маленький белый медвежонок. А как известно, маленькие медвежата в свободное время любят играть в кости на шоколадки.
Одним замечательным солнечным утром, гуляя по льдинам, Мишка встретил своего друга Криса,
которому и предложил сыграть в эту занимательную игру.
Правила её очень просты: сначала определяется значение n — количество раундов игры.
В очередном раунде каждый из игроков один раз бросает стандартный игральный кубик,
на грани которого нанесены различные числа от 1 до 6. Игрок, выбросивший большее значение,
становится победителем в раунде. В случае, если выпавшие значения равны, победа не засчитывается никому.
В самой же игре побеждает участник, выигравший в большем количестве раундов.
Если же количества побед, заслуженных игроками, равны, то объявляется ничья.
Мишка ещё совсем маленький и плохо умеет вести счёт, а потому попросил
Вас понаблюдать за ходом игры и сообщить ему результат.
Входные данные
В первой строке входных данных содержится число n (1 ≤ n ≤ 100) — количество раундов игры.
Следующие n строк содержат описание раундов. В i-й из них содержится пара целых чисел mi и ci
(1 ≤ mi,  ci ≤ 6) — результаты бросков Мишки и Криса в i-ом раунде соответственно.
Выходные данные
В случае победы Мишки в единственной строке выведите "Mishka" (без кавычек),
а в случае победы Криса выведите "Chris" (без кавычек).
Если же игра сведётся к ничьей, то выведите "Friendship is magic!^^" (без кавычек).
PS: генерировать случайные числа(пользоваться модулем random) вам не нужно, данные для игры уже готовы.
Вам нужно только их считать,  и узнать кто же победил"""

m = 0
c = 0

rounds = int(input())
for i in range(rounds):
    mishca, kris = map(int, input().split())
    if mishca > kris:
        m += 1
    elif kris > mishca:
        c += 1

if m > c:
    print('Mishka')
elif c > m:
    print('Chris')
else:
    print('Friendship is magic!^^')
