# Задача по теории вероятностей

# Между двумя берегами реки находятся 6 островов (2 ряда по 3 острова). Между островами и берегами перекинуты мосты. Всего 13 мостов.
# Схема островов и мостов представлена ниже. В случае землетрясения мосты рушатся с вероятностью 1/2. 
# С какой вероятностью человек сможет перейти с берега на берег, если произойдет землетрясение?

# берег
# ------------------------------
# река  |i|     |n|     |s|
#       ---  l  ---  q  ---
#      |   |===|   |===|   |
#       ---     ---     ---
#       |j|     |o|     |t|
#       ---  m  ---  r  ---
#      |   |===|   |===|   |
#       ---     ---     ---
#       |k|     |p|     |u|
# ------------------------------
# берег

# Решение 1:
# Посчитаем, сколько всего может быть комбинаций с разрушенными и/или устоявшими мостами после землетрясения
total_count = 2**13 
print('Количество комбинаций с разрушенными и/или устоявшими мостами:', total_count)

# Перейти с берега на берег, когда все мосты целы, можно 29 способами (10, если начинать с моста i и s, и 9, если начинать с моста n)
# Для каждого способа найдем все комбинации состояний мостов. Пусть 1 означает, что мост цел, и 0, что разрушен

list1 = []
for i in range(1,2):
	for j in range(1,2):
		for k in range(1,2):
			for l in range(2):
				for m in range(2):
					for n in range(2):
						for o in range(2):
							for p in range(2):
								for q in range(2):
									for r in range(2):
										for s in range(2):
											for t in range(2):
												for u in range(2):
													list1.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list2 = []
for i in range(1,2):
	for j in range(1,2):
		for k in range(2):
			for l in range(2):
				for m in range(1,2):
					for n in range(2):
						for o in range(2):
							for p in range(1,2):
								for q in range(2):
									for r in range(2):
										for s in range(2):
											for t in range(2):
												for u in range(2):
													list2.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list3 = []
for i in range(1,2):
	for j in range(1,2):
		for k in range(2):
			for l in range(2):
				for m in range(1,2):
					for n in range(2):
						for o in range(2):
							for p in range(2):
								for q in range(2):
									for r in range(1,2):
										for s in range(2):
											for t in range(2):
												for u in range(1,2):
													list3.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list4 = []
for i in range(1,2):
	for j in range(1,2):
		for k in range(2):
			for l in range(2):
				for m in range(1,2):
					for n in range(2):
						for o in range(1,2):
							for p in range(2):
								for q in range(1,2):
									for r in range(2):
										for s in range(2):
											for t in range(1,2):
												for u in range(1,2):
													list4.append([i,j,k,l,m,n,o,p,q,r,s,t,u])


list5 = []
for i in range(1,2):
	for j in range(2):
		for k in range(2):
			for l in range(1,2):
				for m in range(2):
					for n in range(2):
						for o in range(1,2):
							for p in range(1,2):
								for q in range(2):
									for r in range(2):
										for s in range(2):
											for t in range(2):
												for u in range(2):
													list5.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list6 = []
for i in range(1,2):
	for j in range(2):
		for k in range(1,2):
			for l in range(1,2):
				for m in range(1,2):
					for n in range(2):
						for o in range(1,2):
							for p in range(2):
								for q in range(2):
									for r in range(2):
										for s in range(2):
											for t in range(2):
												for u in range(2):
													list6.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list7 = []
for i in range(1,2):
	for j in range(2):
		for k in range(2):
			for l in range(1,2):
				for m in range(2):
					for n in range(2):
						for o in range(1,2):
							for p in range(2):
								for q in range(2):
									for r in range(1,2):
										for s in range(2):
											for t in range(2):
												for u in range(1,2):
													list7.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list8 = []
for i in range(1,2):
	for j in range(2):
		for k in range(2):
			for l in range(1,2):
				for m in range(2):
					for n in range(2):
						for o in range(2):
							for p in range(2):
								for q in range(1,2):
									for r in range(2):
										for s in range(2):
											for t in range(1,2):
												for u in range(1,2):
													list8.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list9 = []
for i in range(1,2):
	for j in range(2):
		for k in range(2):
			for l in range(1,2):
				for m in range(2):
					for n in range(2):
						for o in range(2):
							for p in range(1,2):
								for q in range(1,2):
									for r in range(1,2):
										for s in range(2):
											for t in range(1,2):
												for u in range(2):
													list9.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list10 = []
for i in range(1,2):
	for j in range(2):
		for k in range(1,2):
			for l in range(1,2):
				for m in range(1,2):
					for n in range(2):
						for o in range(2):
							for p in range(2):
								for q in range(1,2):
									for r in range(1,2):
										for s in range(2):
											for t in range(1,2):
												for u in range(2):
													list10.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list11 = []
for i in range(2):
	for j in range(2):
		for k in range(2):
			for l in range(2):
				for m in range(2):
					for n in range(2):
						for o in range(2):
							for p in range(2):
								for q in range(2):
									for r in range(2):
										for s in range(1, 2):
											for t in range(1, 2):
												for u in range(1, 2):
													list11.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list12 = []
for i in range(2):
	for j in range(2):
		for k in range(2):
			for l in range(2):
				for m in range(2):
					for n in range(2):
						for o in range(2):
							for p in range(1, 2):
								for q in range(2):
									for r in range(1, 2):
										for s in range(1, 2):
											for t in range(1, 2):
												for u in range(2):
													list12.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list13 = []
for i in range(2):
	for j in range(2):
		for k in range(1,2):
			for l in range(2):
				for m in range(1,2):
					for n in range(2):
						for o in range(2):
							for p in range(2):
								for q in range(2):
									for r in range(1,2):
										for s in range(1,2):
											for t in range(1,2):
												for u in range(2):
													list13.append([i,j,k,l,m,n,o,p,q,r,s,t,u])													

list14 = []
for i in range(2):
	for j in range(1,2):
		for k in range(1,2):
			for l in range(1,2):
				for m in range(2):
					for n in range(2):
						for o in range(1,2):
							for p in range(2):
								for q in range(2):
									for r in range(1,2):
										for s in range(1,2):
											for t in range(1,2):
												for u in range(2):
													list14.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list15 = []
for i in range(2):
	for j in range(2):
		for k in range(2):
			for l in range(2):
				for m in range(2):
					for n in range(2):
						for o in range(1,2):
							for p in range(1,2):
								for q in range(1,2):
									for r in range(2):
										for s in range(1, 2):
											for t in range(2):
												for u in range(2):
													list15.append([i,j,k,l,m,n,o,p,q,r,s,t,u])


list16 = []
for i in range(2):
	for j in range(2):
		for k in range(2):
			for l in range(2):
				for m in range(2):
					for n in range(2):
						for o in range(1,2):
							for p in range(2):
								for q in range(1,2):
									for r in range(1,2):
										for s in range(1,2):
											for t in range(2):
												for u in range(1,2):
													list16.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list17 = []
for i in range(2):
	for j in range(2):
		for k in range(1,2):
			for l in range(2):
				for m in range(1,2):
					for n in range(2):
						for o in range(1,2):
							for p in range(2):
								for q in range(1,2):
									for r in range(2):
										for s in range(1,2):
											for t in range(2):
												for u in range(2):
													list17.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list18 = []
for i in range(2):
	for j in range(1,2):
		for k in range(1,2):
			for l in range(1,2):
				for m in range(2):
					for n in range(2):
						for o in range(2):
							for p in range(2):
								for q in range(1,2):
									for r in range(2):
										for s in range(1,2):
											for t in range(2):
												for u in range(2):
													list18.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list19 = []
for i in range(2):
	for j in range(1,2):
		for k in range(2):
			for l in range(1,2):
				for m in range(1,2):
					for n in range(2):
						for o in range(2):
							for p in range(1,2):
								for q in range(1,2):
									for r in range(2):
										for s in range(1,2):
											for t in range(2):
												for u in range(2):
													list19.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list20 = []
for i in range(2):
	for j in range(1,2):
		for k in range(2):
			for l in range(1,2):
				for m in range(1,2):
					for n in range(2):
						for o in range(2):
							for p in range(2):
								for q in range(1,2):
									for r in range(1,2):
										for s in range(1,2):
											for t in range(2):
												for u in range(1,2):
													list20.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list21 = []
for i in range(2):
	for j in range(2):
		for k in range(2):
			for l in range(2):
				for m in range(2):
					for n in range(1,2):
						for o in range(1,2):
							for p in range(1,2):
								for q in range(2):
									for r in range(2):
										for s in range(2):
											for t in range(2):
												for u in range(2):
													list21.append([i,j,k,l,m,n,o,p,q,r,s,t,u])


list22 = []
for i in range(2):
	for j in range(1,2):
		for k in range(1,2):
			for l in range(1,2):
				for m in range(2):
					for n in range(1,2):
						for o in range(2):
							for p in range(2):
								for q in range(2):
									for r in range(2):
										for s in range(2):
											for t in range(2):
												for u in range(2):
													list22.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list23 = []
for i in range(2):
	for j in range(1,2):
		for k in range(2):
			for l in range(1,2):
				for m in range(1,2):
					for n in range(1,2):
						for o in range(2):
							for p in range(1,2):
								for q in range(2):
									for r in range(2):
										for s in range(2):
											for t in range(2):
												for u in range(2):
													list23.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list24 = []
for i in range(2):
	for j in range(1,2):
		for k in range(2):
			for l in range(1,2):
				for m in range(1,2):
					for n in range(1,2):
						for o in range(2):
							for p in range(2):
								for q in range(2):
									for r in range(1,2):
										for s in range(2):
											for t in range(2):
												for u in range(1,2):
													list24.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list25 = []
for i in range(2):
	for j in range(2):
		for k in range(2):
			for l in range(2):
				for m in range(2):
					for n in range(1,2):
						for o in range(2):
							for p in range(2):
								for q in range(1,2):
									for r in range(2):
										for s in range(2):
											for t in range(1,2):
												for u in range(1,2):
													list25.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list26 = []
for i in range(2):
	for j in range(2):
		for k in range(2):
			for l in range(2):
				for m in range(2):
					for n in range(1,2):
						for o in range(2):
							for p in range(1,2):
								for q in range(1,2):
									for r in range(1,2):
										for s in range(2):
											for t in range(1,2):
												for u in range(2):
													list26.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list27 = []
for i in range(2):
	for j in range(2):
		for k in range(1,2):
			for l in range(2):
				for m in range(1,2):
					for n in range(1,2):
						for o in range(1,2):
							for p in range(2):
								for q in range(2):
									for r in range(2):
										for s in range(2):
											for t in range(2):
												for u in range(2):
													list27.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list28 = []
for i in range(2):
	for j in range(2):
		for k in range(1,2):
			for l in range(2):
				for m in range(1,2):
					for n in range(1,2):
						for o in range(2):
							for p in range(2):
								for q in range(1,2):
									for r in range(1,2):
										for s in range(2):
											for t in range(1,2):
												for u in range(2):
													list28.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

list29 = []
for i in range(2):
	for j in range(2):
		for k in range(2):
			for l in range(2):
				for m in range(2):
					for n in range(1,2):
						for o in range(1,2):
							for p in range(2):
								for q in range(2):
									for r in range(1,2):
										for s in range(2):
											for t in range(2):
												for u in range(1,2):
													list29.append([i,j,k,l,m,n,o,p,q,r,s,t,u])

# Так как списки комбинаций способов перейти реку имеют пересечения, то найдем их и удалим дубли

def foo(listx, listy):
	for i in range(len(listx)):
		for j in range(len(listy)):
			if listx[i] == listy[j]:
				del listx[i]
				listx.insert(i, 'shit') # добавим элемент, который позволит сохранить нумерацию в списках и который можно будет легко найти в будущем			
	cnt = listx.count('shit')
	for i in range(cnt):
		listx.remove('shit')

foo(list1, list2)
foo(list1, list3)
foo(list1, list4)
foo(list1, list5)
foo(list1, list6)
foo(list1, list7)
foo(list1, list8)
foo(list1, list9)
foo(list1, list10)
foo(list1, list11)
foo(list1, list12)
foo(list1, list13)
foo(list1, list14)
foo(list1, list15)
foo(list1, list16)
foo(list1, list17)
foo(list1, list18)
foo(list1, list19)
foo(list1, list20)
foo(list1, list21)
foo(list1, list22)
foo(list1, list23)
foo(list1, list24)
foo(list1, list25)
foo(list1, list26)
foo(list1, list27)
foo(list1, list28)
foo(list1, list29)

foo(list2, list3)
foo(list2, list4)
foo(list2, list5)
foo(list2, list6)
foo(list2, list7)
foo(list2, list8)
foo(list2, list9)
foo(list2, list10)
foo(list2, list11)
foo(list2, list12)
foo(list2, list13)
foo(list2, list14)
foo(list2, list15)
foo(list2, list16)
foo(list2, list17)
foo(list2, list18)
foo(list2, list19)
foo(list2, list20)
foo(list2, list21)
foo(list2, list22)
foo(list2, list23)
foo(list2, list24)
foo(list2, list25)
foo(list2, list26)
foo(list2, list27)
foo(list2, list28)
foo(list2, list29)

foo(list3, list4)
foo(list3, list5)
foo(list3, list6)
foo(list3, list7)
foo(list3, list8)
foo(list3, list9)
foo(list3, list10)
foo(list3, list11)
foo(list3, list12)
foo(list3, list13)
foo(list3, list14)
foo(list3, list15)
foo(list3, list16)
foo(list3, list17)
foo(list3, list18)
foo(list3, list19)
foo(list3, list20)
foo(list3, list21)
foo(list3, list22)
foo(list3, list23)
foo(list3, list24)
foo(list3, list25)
foo(list3, list26)
foo(list3, list27)
foo(list3, list28)
foo(list3, list29)

foo(list4, list5)
foo(list4, list6)
foo(list4, list7)
foo(list4, list8)
foo(list4, list9)
foo(list4, list10)
foo(list4, list11)
foo(list4, list12)
foo(list4, list13)
foo(list4, list14)
foo(list4, list15)
foo(list4, list16)
foo(list4, list17)
foo(list4, list18)
foo(list4, list19)
foo(list4, list20)
foo(list4, list21)
foo(list4, list22)
foo(list4, list23)
foo(list4, list24)
foo(list4, list25)
foo(list4, list26)
foo(list4, list27)
foo(list4, list28)
foo(list4, list29)

foo(list5, list6)
foo(list5, list7)
foo(list5, list8)
foo(list5, list9)
foo(list5, list10)
foo(list5, list11)
foo(list5, list12)
foo(list5, list13)
foo(list5, list14)
foo(list5, list15)
foo(list5, list16)
foo(list5, list17)
foo(list5, list18)
foo(list5, list19)
foo(list5, list20)
foo(list5, list21)
foo(list5, list22)
foo(list5, list23)
foo(list5, list24)
foo(list5, list25)
foo(list5, list26)
foo(list5, list27)
foo(list5, list28)
foo(list5, list29)

foo(list6, list7)
foo(list6, list8)
foo(list6, list9)
foo(list6, list10)
foo(list6, list11)
foo(list6, list12)
foo(list6, list13)
foo(list6, list14)
foo(list6, list15)
foo(list6, list16)
foo(list6, list17)
foo(list6, list18)
foo(list6, list19)
foo(list6, list20)
foo(list6, list21)
foo(list6, list22)
foo(list6, list23)
foo(list6, list24)
foo(list6, list25)
foo(list6, list26)
foo(list6, list27)
foo(list6, list28)
foo(list6, list29)

foo(list7, list8)
foo(list7, list9)
foo(list7, list10)
foo(list7, list11)
foo(list7, list12)
foo(list7, list13)
foo(list7, list14)
foo(list7, list15)
foo(list7, list16)
foo(list7, list17)
foo(list7, list18)
foo(list7, list19)
foo(list7, list20)
foo(list7, list21)
foo(list7, list22)
foo(list7, list23)
foo(list7, list24)
foo(list7, list25)
foo(list7, list26)
foo(list7, list27)
foo(list7, list28)
foo(list7, list29)

foo(list8, list9)
foo(list8, list10)
foo(list8, list11)
foo(list8, list12)
foo(list8, list13)
foo(list8, list14)
foo(list8, list15)
foo(list8, list16)
foo(list8, list17)
foo(list8, list18)
foo(list8, list19)
foo(list8, list20)
foo(list8, list21)
foo(list8, list22)
foo(list8, list23)
foo(list8, list24)
foo(list8, list25)
foo(list8, list26)
foo(list8, list27)
foo(list8, list28)
foo(list8, list29)

foo(list9, list10)
foo(list9, list11)
foo(list9, list12)
foo(list9, list13)
foo(list9, list14)
foo(list9, list15)
foo(list9, list16)
foo(list9, list17)
foo(list9, list18)
foo(list9, list19)
foo(list9, list20)
foo(list9, list21)
foo(list9, list22)
foo(list9, list23)
foo(list9, list24)
foo(list9, list25)
foo(list9, list26)
foo(list9, list27)
foo(list9, list28)
foo(list9, list29)

foo(list10, list11)
foo(list10, list12)
foo(list10, list13)
foo(list10, list14)
foo(list10, list15)
foo(list10, list16)
foo(list10, list17)
foo(list10, list18)
foo(list10, list19)
foo(list10, list20)
foo(list10, list21)
foo(list10, list22)
foo(list10, list23)
foo(list10, list24)
foo(list10, list25)
foo(list10, list26)
foo(list10, list27)
foo(list10, list28)
foo(list10, list29)

foo(list11, list12)
foo(list11, list13)
foo(list11, list14)
foo(list11, list15)
foo(list11, list16)
foo(list11, list17)
foo(list11, list18)
foo(list11, list19)
foo(list11, list20)
foo(list11, list21)
foo(list11, list22)
foo(list11, list23)
foo(list11, list24)
foo(list11, list25)
foo(list11, list26)
foo(list11, list27)
foo(list11, list28)
foo(list11, list29)

foo(list12, list13)
foo(list12, list14)
foo(list12, list15)
foo(list12, list16)
foo(list12, list17)
foo(list12, list18)
foo(list12, list19)
foo(list12, list20)
foo(list12, list21)
foo(list12, list22)
foo(list12, list23)
foo(list12, list24)
foo(list12, list25)
foo(list12, list26)
foo(list12, list27)
foo(list12, list28)
foo(list12, list29)

foo(list13, list14)
foo(list13, list15)
foo(list13, list16)
foo(list13, list17)
foo(list13, list18)
foo(list13, list19)
foo(list13, list20)
foo(list13, list21)
foo(list13, list22)
foo(list13, list23)
foo(list13, list24)
foo(list13, list25)
foo(list13, list26)
foo(list13, list27)
foo(list13, list28)
foo(list13, list29)

foo(list14, list15)
foo(list14, list16)
foo(list14, list17)
foo(list14, list18)
foo(list14, list19)
foo(list14, list20)
foo(list14, list21)
foo(list14, list22)
foo(list14, list23)
foo(list14, list24)
foo(list14, list25)
foo(list14, list26)
foo(list14, list27)
foo(list14, list28)
foo(list14, list29)

foo(list15, list16)
foo(list15, list17)
foo(list15, list18)
foo(list15, list19)
foo(list15, list20)
foo(list15, list21)
foo(list15, list22)
foo(list15, list23)
foo(list15, list24)
foo(list15, list25)
foo(list15, list26)
foo(list15, list27)
foo(list15, list28)
foo(list15, list29)

foo(list16, list17)
foo(list16, list18)
foo(list16, list19)
foo(list16, list20)
foo(list16, list21)
foo(list16, list22)
foo(list16, list23)
foo(list16, list24)
foo(list16, list25)
foo(list16, list26)
foo(list16, list27)
foo(list16, list28)
foo(list16, list29)

foo(list17, list18)
foo(list17, list19)
foo(list17, list20)
foo(list17, list21)
foo(list17, list22)
foo(list17, list23)
foo(list17, list24)
foo(list17, list25)
foo(list17, list26)
foo(list17, list27)
foo(list17, list28)
foo(list17, list29)

foo(list18, list19)
foo(list18, list20)
foo(list18, list21)
foo(list18, list22)
foo(list18, list23)
foo(list18, list24)
foo(list18, list25)
foo(list18, list26)
foo(list18, list27)
foo(list18, list28)
foo(list18, list29)

foo(list19, list20)
foo(list19, list21)
foo(list19, list22)
foo(list19, list23)
foo(list19, list24)
foo(list19, list25)
foo(list19, list26)
foo(list19, list27)
foo(list19, list28)
foo(list19, list29)

foo(list20, list21)
foo(list20, list22)
foo(list20, list23)
foo(list20, list24)
foo(list20, list25)
foo(list20, list26)
foo(list20, list27)
foo(list20, list28)
foo(list20, list29)

foo(list21, list22)
foo(list21, list23)
foo(list21, list24)
foo(list21, list25)
foo(list21, list26)
foo(list21, list27)
foo(list21, list28)
foo(list21, list29)

foo(list22, list23)
foo(list22, list24)
foo(list22, list25)
foo(list22, list26)
foo(list22, list27)
foo(list22, list28)
foo(list22, list29)

foo(list23, list24)
foo(list23, list25)
foo(list23, list26)
foo(list23, list27)
foo(list23, list28)
foo(list23, list29)

foo(list24, list25)
foo(list24, list26)
foo(list24, list27)
foo(list24, list28)
foo(list24, list29)

foo(list25, list26)
foo(list25, list27)
foo(list25, list28)
foo(list25, list29)

foo(list26, list27)
foo(list26, list28)
foo(list26, list29)

foo(list27, list28)
foo(list27, list29)

foo(list28, list29)

# Посчитаем количество комбинаций для каждого способа перейти реку (после чистки от дублей)

l1 = len(list1)
l2 = len(list2)
l3 = len(list3)
l4 = len(list4)
l5 = len(list5)
l6 = len(list6)
l7 = len(list7)
l8 = len(list8)
l9 = len(list9)
l10 = len(list10)
l11 = len(list11)
l12 = len(list12)
l13 = len(list13)
l14 = len(list14)
l15 = len(list15)
l16 = len(list16)
l17 = len(list17)
l18 = len(list18)
l19 = len(list19)
l20 = len(list20)
l21 = len(list21)
l22 = len(list22)
l23 = len(list23)
l24 = len(list24)
l25 = len(list25)
l26 = len(list26)
l27 = len(list27)
l28 = len(list28)
l29 = len(list29)

# Найдем суммарное количество комбинаций с разрушенными и/или устоявшими мостами, при которых можно перейти реку
count_positive = l1+l2+l3+l4+l5+l6+l7+l8+l9+l10+l11+l12+l13+l14+l15+l16+l17+l18+l19+l20+l21+l22+l23+l24+l25+l26+l27+l28+l29
print('Количество комбинаций с разрушенными и/или устоявшими мостами, когда можно перейти реку:', count_positive)

# Найдем вероятность перейти реку согласно частотному определению вероятности (количество успешных комбинаций/суммарное количество комбинаций)
P = count_positive/total_count
print('Вероятность перейти реку в случае землетрясения:', P)

# Решение 2:
# Эту задачу можно решить безо всяких формул и расчетов примерно за 1 минуту. Попробуйте найти это решение.