# Портфолио моих проектов в области Data Analysis

| Проект | Описание | Инструменты |
|----------------|---------|----------------|
| [Событийный анализ и A/A/B-тест в мобильном приложении](https://github.com/OlegDze/public/blob/main/event_analysis_and_aab_test.ipynb) | По заказу магазина продуктов питания нужно разобраться, как ведут себя пользователи его мобильного приложения. Необходимо изучить воронку продаж: узнать, сколько пользователей доходят до покупки и сколько - «застревает» на предыдущих шагах. Также необходимо изучить результаты A/A/B-эксперимента, в ходе которого в приложении были изменены шрифты.  | `Python, pandas, matplotlib, statsmodels`, A/A/B-тест, z-критерий, критерий χ2 |
| [Приоритизация гипотез и A/B-тест в интернет-магазине](https://github.com/OlegDze/public/blob/main/hypotheses_prioritization_and_ab_test.ipynb) | Для отдела маркетинга интернет-магазина нужно провести приоритизацию гипотез по увеличению выручки. После выбора наиболее важной гипотезы и её проверки в течение месяца с помощью A/B-теста, нужно проанализировать результаты и принять решение об остановке или продолжении теста. | `Python, pandas, matplotlib, scipy, statsmodels`, фреймворки ICE и RICE, A/B-тест, критерий Манна-Уитни, z-критерий |
| [Когортный анализ и сравнение источников трафика](https://github.com/OlegDze/public/blob/main/cohort_and_traffic_sources_analysis.ipynb) | Для отдела маркетинговой аналитики Яндекс.Афиши необходимо подготовить отчёт, который поможет маркетологам снизить расходы — отказаться от невыгодных источников трафика и перераспределить бюджет. | `Python, pandas, matplotlib, seaborn`, когортный анализ, расчёт метрик DAU, Retention Rate, ASL, LTV, CAC, ROMI |
| [Анализ рынка заведений общественного питания Москвы](https://github.com/OlegDze/public/blob/main/public_catering_analysis.ipynb) | Перед открытием нового объекта общественного питания в Москве необходимо провести исследование рынка уже функционирующих заведений. Нужно определить востребованный вид заведения, размер (количество посадочных мест) и район города. В качестве исходной информации есть открытые данные о заведениях общественного питания в Москве. | `Python, pandas, matplotlib, seaborn, plotly`, обработка скрытых дублей, подготовка презентации |
| [Анализ ассортимента магазина товаров для дома](https://github.com/OlegDze/public/blob/main/product_categorization.ipynb) | Необходимо провести анализ ассортимента интернет-магазина товаров для дома и быта «Пока все ещё тут». В рамках анализа нужно выделить категории товаров, выделить основной и дополнительный ассортименты внутри категорий, выдвинуть гипотезу о различиях между основным и дополнительным ассортиментами и проверить её. | `Python, pandas, matplotlib`, KMeans для кластеризации, z-критерий, Tableau, подготовка презентации |
| [A/B-тест рекомендательной системы](https://github.com/OlegDze/public/blob/main/recommendation_system_ab_test.ipynb) | Необходимо оценить корректность проведения A/B-теста, отфильтровать всех неподходящих участников и проанализировать результаты. | `Python, pandas, matplotlib, statsmodels`, A/B-тест, z-критерий |
| [Исследование компьютерных игр](https://github.com/OlegDze/public/blob/main/computer_games_analysis.ipynb) | Интернет-магазин «World of games» продаёт по всему миру компьютерные игры. По его заказу необходимо выявить определяющие успешность игры закономерности, чтобы сделать ставку на потенциально популярный продукт и спланировать рекламные кампании. | `Python, pandas, matplotlib, stats`, восстановление пропущенных данных, корреляционный анализ, t-критерий Уэлча |
| [Исследование объявлений о продаже квартир в Санкт-Петербурге](https://github.com/OlegDze/public/blob/main/real_estate_analysis.ipynb) | Сервис Яндекс.Недвижимость размещает объявления о продаже квартир. По его заказу нужно проанализировать рынок недвижимости в Санкт-Петербурге и соседних населённых пунктах и определить влияние различных параметров на цену квартир. | `Python, pandas, matplotlib`, обработка скрытых дублей и артефактов, восстановление пропущенных данных, корреляционный анализ |
| [Сравнительный анализ доходности тарифов сотовой связи](https://github.com/OlegDze/public/blob/main/cellular_tariffs_analysis.ipynb) | Клиентам оператора сотовой связи «Мегалайна» предлагают два тарифных плана: «Смарт» и «Ультра». Чтобы скорректировать рекламный бюджет, коммерческий департамент хочет понять, какой тариф приносит больше денег. Для этого необходимо сделать предварительный анализ тарифов на небольшой выборке клиентов. | `Python, pandas, matplotlib, stats`, t-критерий Стьюдента |

# Портфолио моих проектов в области Machine Learning
| Проект | Описание | Инструменты |
|----------------|---------|----------------|
| [Предсказание оттока и повышение качества работы с клиентами фитнес-центра](https://github.com/OlegDze/public/blob/main/gym_churn_prediction.ipynb) | Сеть фитнес-центров "Культурист-датасаентист" разрабатывает стратегию взаимодействия с клиентами на основе аналитических данных. Стратегия направлена на борьбу с оттоком клиентов. Необходимо научиться прогнозировать вероятность оттока для каждого клиента, выделить несколько наиболее ярких групп клиентов, сформулировать рекомендации по повышению качества работы с клиентами.  | `Python, pandas, matplotlib, seaborn, sklearn`, LogisticRegression и RandomForestClassifier для бинарной классификации, linkage и KMeans для кластеризации |
| [Предсказание успешности прохождения пользователями он-лайн курса на stepik](https://github.com/OlegDze/public/blob/main/stepik_ml_contest.ipynb) | Необходимо построить модель, которая бы предсказывала по активности нового пользователя в первые 2 дня обучения на онлайн курсе "Введение в анализ данных в R", пройдёт ли он этот курс в итоге или нет. Качество прогноза модели оценивается по значению ROC AUC. Задача взята из курса "Введение в Data Science и машинное обучение" на stepik.  | `Python, pandas, matplotlib, sklearn`, алгоритмы бинарной классификации |

# Портфолио задач по SQL
| Проект | Описание |
|----------------|---------|
| [Решения задач с сайта sql-ex.ru](https://github.com/OlegDze/public/blob/main/sql_ex_solutions.md) | Первые 60 задач с сайта sql-ex.ru на 11 июля 2021 и решения для них. |
