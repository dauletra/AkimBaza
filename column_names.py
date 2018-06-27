"""
KPU_SRN

Имя Колонки	Порядковый Номер	Тип Данных	Charset	Длина	Масштаб	Не Null	Авто генерация	Auto увеличение	По умолчанию	Ключ	Описание
ID	1	INTEGER	[NULL]	10	[NULL]	true	false	false	[NULL]	false
ID_KPU_CATAL	2	INTEGER	[NULL]	10	[NULL]	true	false	false	[NULL]	false
POR_NOM	3	INTEGER	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
FAM	4	VARCHAR	UTF-8	100	[NULL]	false	false	false	[NULL]	false	[NULL]
IM	5	VARCHAR	UTF-8	100	[NULL]	false	false	false	[NULL]	false	[NULL]
OT	6	VARCHAR	UTF-8	100	[NULL]	false	false	false	[NULL]	false	[NULL]
IIN	7	VARCHAR	UTF-8	13	[NULL]	false	false	false	[NULL]	false	[NULL]
SROGD_ID	8	INTEGER	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
NUM_RODI	9	INTEGER	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
NUM_SUPR	10	INTEGER	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
POL_SPP_ID	11	INTEGER	[NULL]	10	[NULL]	false	false	false	[NULL]	false
KN_ID	12	INTEGER	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
DATE_R	13	DATE	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
DATE_SM	14	DATE	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
DATE_F_BR	15	DATE	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
DATE_VD	16	DATE	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
DATE_RAZV	17	DATE	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
DATE_L_BR	18	DATE	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
DATE_IN	19	DATE	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
DATE_OUT	20	DATE	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
SUODH_ID	21	INTEGER	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
SOOO_ID	22	INTEGER	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
PZ_ID	23	INTEGER	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
SID_ID	24	INTEGER	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
SID2_ID	25	INTEGER	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
SID3_ID	26	INTEGER	[NULL]	10	[NULL]	false	false	false	[NULL]	false	[NULL]
DATE_ACTUAL	27	TIMESTAMP	[NULL]	19	[NULL]	false	false	false	[NULL]	false	[NULL]
IS_TEMP	28	SMALLINT	[NULL]	5	[NULL]	false	false	false	[NULL]	false	[NULL]
IS_TEMP_OUT	29	SMALLINT	[NULL]	5	[NULL]	false	false	false	[NULL]	false	[NULL]


KPU_SPR_SUODH
1	дошкольная	мектепке дейінгі	1
2	начальное	бастауыш	2
3	основное среднее	негізгі орта	3
4	общее среднее	жалпы орта	4
5	начальное профессиональное	бастауыш кәсіптік	5
6	среднее специальное	орта арнаулы	6
7	незаконченное высшее	аяқталмаған жоғары	7
8	высшее	жоғары	8
9	не имеют начального	бастауыш білімі жоқ	9
0	не достигнут никакой уровень образования	ешқандай білім деңгейіне қол жеткізбеген	0


KPU_SPR_SOOO
1	дошкольная	мектепке дейінгі	1
2	общеобразовательная школа	жалпы білім беретін мектеп	2
3	технического и профессионального	техникалық және кәсіптік	3
4	ВУЗ	ЖОО	4
5	послевузовская	жоғары оқу орнынан кейінгі	5
6	курсы повышения квалификации	біліктілікті көтеру курстар	6


KPU_SPR_PZ
1	работающий по найму	жалдамалы қызметкер	1
2	работодатель	жұмыс беруші	2
3	занятый на индивидуальной основе	жеке негізде жұмыс істеуші	3
4	занятый в личном подсобном хозяйстве производством продукции для продажи (обмена)	жеке қосалқы шаруашылықта (жеке аулада) өнімді сату (айырбас) үшін өндірумен айналысатын жұмыспен қамтылған	4
5	член кооператива	кооператив мүшесі	5
6	помогающий (неоплачиваемый) работник семейного предприятия	отбасылық кәсіпорындардың көмектесетін (ақы төленбейтін) қызметкері	6
7	безработный	жұмыссыз	7
8	лицо не входящее в состав рабочей силы	жұмыс күші құрамына кірмейтін тұлға	8


KPU_SPR_SID
1	доход от работ по найму	жалдамалы жұмыстан табыс	1
2	доход от самостоятельной занятости (кроме работы в личном подсобным хозяйстве)	өз бетінше жұмыс істеуден табыс (жеке қосалқы шаруашылықтағы жұмыстан басқа)	2
3	работа в личном подсобным хозяйстве	жеке қосалқы шаруашылықтағы жұмыс	3
4	стипендия	стипендия	4
5	пенсия	зейнетақы	5
6	пособие	жәрдемақы	6
7	материальная помощь от родных или близких	туысқан немесе жақындардан көмек	7
8	доход от собственности, дивиденды, вознаграждения	жеке меншіктен табыс, дивидент, сыйақылар	8
9	иждивенец	асыраудағы	9
10	иное	өзге	10
"""
