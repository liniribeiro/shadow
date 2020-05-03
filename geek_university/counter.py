from collections import Counter

counter_list = [1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 5, 6, 7, 8, 8, 8, 4, 5, 4, 5, 45]

res = Counter(counter_list)

print(res)

print(Counter("alini"))

big_text = """Ferdinand Maximilien de Habsbourg-Lorraine, né à Vienne (Autriche) le 6 juillet 1832 et mort fusillé au Cerro de las Campanas à Santiago de Querétaro (Mexique) le 19 juin 1867, est un archiduc d'Autriche, prince royal de Hongrie et de Bohême, devenu empereur du Mexique sous le nom de Maximilien Ier en 1864. Frère cadet de l'empereur d'Autriche François-Joseph Ier, il épouse en 1857 la princesse Charlotte de Belgique.

En 1857, Maximilien est nommé vice-roi du royaume de Lombardie-Vénétie que l'Autriche a acquis au congrès de Vienne et qui se montre rebelle au pouvoir de la maison de Habsbourg. Sa politique trop libérale aux yeux du pouvoir autrichien, son indulgence envers les rebelles italiens et sa prodigalité le contraignent à la démission le 10 avril 1859.

Lors de l'expédition du Mexique qui débute au cours de l'hiver 1861-1862, la France, alliée à l'Espagne et au Royaume-Uni, envahit la République mexicaine. Les Espagnols et les Britanniques se retirent en avril 1862, tandis que l'armée française demeure sur place, cherchant à conquérir le pays. Désireux de légitimer cette domination, Napoléon III soutient un groupe de monarchistes """


words = big_text.split()
print(words)

res = Counter(words)
print(res)

# as 5 palavras com mais ocorrencia no texto

print(res.most_common(5))

