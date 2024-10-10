# goit-algo-hw-04

# Домашнє завдання: Порівняння алгоритмів сортування

## Вступ

У цьому домашньому завданні ми порівнювали три алгоритми сортування: **злиттям**, **вставками** та **Timsort** (вбудований алгоритм Python). Основною метою було оцінити їх ефективність на різних наборах даних та перевірити теоретичні оцінки складності.

## Ефективність алгоритмів

1. **Сортування злиттям**: продемонструвало стабільну ефективність з часовою складністю \(O(n \log n)\) на всіх наборах даних. Найкраще підходить для великих масивів.

2. **Сортування вставками**: показало хорошу продуктивність на малих та відсортованих масивах, але значно сповільнювалося на великих або випадкових масивах через складність \(O(n^2)\).

3. **Timsort**: показав найкращі результати на реальних і частково відсортованих наборах даних завдяки поєднанню сильних сторін сортування злиттям та вставками. Це робить його ефективним для більшості практичних випадків.

## Висновки

Алгоритм **Timsort**, завдяки поєднанню двох підходів, є найкращим вибором для загального сортування в Python. Його продуктивність перевершує окремі алгоритми завдяки адаптивності та ефективності на реальних даних.
