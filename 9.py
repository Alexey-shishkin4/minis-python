def format_table(benchmarks, algos, results):
    benchmarks.append('Benchmark')
    col_width = [len(max(benchmarks, key=len))]
    for i in range(len(algos)):
        col_width.append(len(max((algos[i], *[str(results[j][i]) for j in range(len(benchmarks[:-1]))]), key=len)))
    print(col_width)

    print('Benchmark'.ljust(col_width[0]) + '| ' + ' | '.join(str(algos[i]).ljust(col_width[i + 1])
                                                              for i in range(len(algos))) + ' |')
    print('|' + '-' * (sum(col_width) + len(col_width) * 2) + '|')
    for i in range(len(benchmarks[:-1])):
        print(benchmarks[i].ljust(col_width[0]) + '| ' + ' | '.join(str(results[i][j]).ljust(col_width[j + 1])
                                                                    for j in range(len(results[i]))) + ' |')


format_table(["best case", "the worst case", "normal case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9], [1, 2.0, 3.141341232432414]])


format_table(["best case", "the worst case"],
             ["quick sort", "merge sort", "bubble sort"],
             [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
