const activities = [
  {
    id: 1,
    name: "Мечеть «Сердце Чечни»",
    imgs: [
      { url: "https://russiantour.net/images/gallery/elements/en/23bf9b8d53e75867d39e5af15709898a.jpg", is_main: true },
      { url: "https://a.d-cd.net/5hAAAgKnX-A-1920.jpg", is_main: false },
      { url: "https://imgbb.ru/frontend/posts/creation/2022-10-17/vbnqnsmr9qsox3er27ujqpmccdn0ywi43mn.jpg", is_main: false }
    ],
    mood: ["спокойное", "умиротворенное"],
    time: "среднее",
    budget: "бесплатно",
    category: "религия"
  },
  {
    id: 2,
    name: "Грозный-Сити",
    imgs: [
      { url: "https://mkm-metal.ru/upload/iblock/c53/Groznyy-Siti.jpg", is_main: true },
      { url: "https://cdn.culture.ru/images/3a97e571-37c6-5394-819a-1dfe6358ad7e", is_main: false },
      { url: "https://travelbelka.ru/wp-content/uploads/2024/06/Groznyy_Siti-nochyu.jpeg", is_main: false }
    ],
    mood: ["романтическое", "вдохновляющее"],
    time: "среднее",
    budget: "дешево",
    category: "архитектура"
  },
  {
    id: 3,
    name: "Национальный музей ЧР",
    imgs: [
      { url: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Музей_Чеченской_Республики.jpg/1600px-Музей_Чеченской_Республики.jpg", is_main: true },
      { url: "https://pic.rutubelist.ru/video/8f/86/8f86a77201dcfbad141d0f7dfcb3001a.jpg", is_main: false },
      { url: "https://www.grozny-inform.ru/LoadedImages/2020/11/30/16184811202447421_114d.jpg", is_main: false }
    ],
    mood: ["познавательное", "серьезное"],
    time: "долгое",
    budget: "дешево",
    category: "культура"
  },
  {
    id: 4,
    name: "Парк имени А. Кадырова",
    imgs: [
      { url: "http://ic.pics.livejournal.com/kukmor/14257925/2087103/2087103_original.jpg", is_main: true },
      { url: "https://cdttk.dod95.ru/images/photos/article_cdttk_378.jpg", is_main: false },
      { url: "https://www.grozny-inform.ru/LoadedFiles/0s193/43_w1000_h700.jpg", is_main: false }
    ],
    mood: ["семейное", "радостное"],
    time: "среднее",
    budget: "бесплатно",
    category: "отдых"
  },
  {
    id: 5,
    name: "Проспект В.В. Путина",
    imgs: [
      { url: "https://cdn.culture.ru/images/bef55047-885f-529d-b220-dcc0a25616b5", is_main: true },
      { url: "https://s.101hotelscdn.ru/uploads/image/hotel_image/15339/3294195.jpg", is_main: false },
      { url: "https://ic.pics.livejournal.com/bepowerback/76977204/875495/875495_original.jpg", is_main: false }
    ],
    mood: ["прогулочное", "нейтральное"],
    time: "короткое",
    budget: "бесплатно",
    category: "город"
  },
  {
    id: 6,
    name: "Озеро «Грозненское море»",
    imgs: [
      { url: "https://avatars.mds.yandex.net/i?id=ee3371eeeb9b91fd5149cb52080b081d_l-4979658-images-thumbs&n=13", is_main: true },
      { url: "https://avatars.mds.yandex.net/get-altay/5265775/2a0000017c16087c82e8978833e016255821/XXL_height", is_main: false },
      { url: "https://www.grozny-inform.ru/LoadedFiles/new/3_w1000_h700.jpg", is_main: false }
    ],
    mood: ["спокойное", "романтическое"],
    time: "долгое",
    budget: "дешево",
    category: "природа"
  },
  {
    id: 7,
    name: "Ресторан Benefis",
    imgs: [
      { url: "https://avatars.mds.yandex.net/get-altay/5448678/2a0000017cf5521465bd89768741f06be552/XXL", is_main: true },
      { url: "https://avatars.mds.yandex.net/i?id=74c6e6ab3dfd49a3b8e1dcfb4487dec850bc29f8-9706559-images-thumbs&n=13", is_main: false },
      { url: "https://monplezir.pro/upload/resize_cache/iblock/ce0/1200_800_1/ypcgxgz6hampcbbedhs0y1t4wehdlvml.JPG", is_main: false }
    ],
    mood: ["праздничное", "гастрономическое"],
    time: "долгое",
    budget: "дорого",
    category: "еда"
  },
  {
    id: 8,
    name: "Чеченская государственная филармония",
    imgs: [
      { url: "https://cdn.culture.ru/images/4ea5b906-f017-5324-a4b2-5821967e9a35", is_main: true },
      { url: "https://grozny.tv/storage/images/05fac51fdd640147.jpeg", is_main: false },
      { url: "http://img.tourister.ru/files/3/2/5/3/6/1/9/7/original.jpg", is_main: false }
    ],
    mood: ["культурное", "эстетическое"],
    time: "долгое",
    budget: "дешево",
    category: "искусство"
  },
  {
    id: 9,
    name: "Мемориальный комплекс Славы",
    imgs: [
      { url: "https://cdn.culture.ru/images/e7a81880-3fe8-5800-b4e2-826b5935a695", is_main: true },
      { url: "https://grozny.etokavkaz.ru/images/memorial_5.jpg", is_main: false },
      { url: "https://cdn.culture.ru/c/758681.jpg", is_main: false }
    ],
    mood: ["патриотическое", "серьезное"],
    time: "среднее",
    budget: "бесплатно",
    category: "история"
  },
  {
    id: 10,
    name: "Грозненский русский драматический театр",
    imgs: [
      { url: "https://cdn.culture.ru/c/761909.jpg", is_main: true },
      { url: "https://varlamov.me/2016/grozniy_hor/14.jpg", is_main: false },
      { url: "https://avatars.mds.yandex.net/get-altay/1545421/2a0000016ae33079fb009b85730e3437865c/diploma", is_main: false }
    ],
    mood: ["культурное", "развлекательное"],
    time: "долгое",
    budget: "дешево",
    category: "театр"
  },
  {
    id: 11,
    name: "Цветочный парк",
    imgs: [
      { url: "https://grozny-inform.ru/LoadedImages/2025/04/03/Izobrazhenie_WhatsApp_2025-04-03_v_16.23.52_77988737.jpg", is_main: true },
      { url: "https://i.ytimg.com/vi/XAmMdM0Wcso/maxresdefault.jpg", is_main: false },
      { url: "https://img.tourister.ru/files/2/1/3/1/1/6/0/9/original.jpg", is_main: false }
    ],
    mood: ["романтическое", "спокойное"],
    time: "короткое",
    budget: "бесплатно",
    category: "природа"
  },
  {
    id: 12,
    name: "ТРЦ «Грозный Молл»",
    imgs: [
      { url: "https://www.grozny-inform.ru/LoadedFiles/0a103/13_w1000_h700.jpg", is_main: true },
      { url: "https://cre.ru/content/upload/news/big/16608993150881.jpg", is_main: false },
      { url: "https://avatars.mds.yandex.net/get-altay/11421964/2a0000018bc53eed5caad306f7ff1e8050f3/XXL_height", is_main: false }
    ],
    mood: ["развлекательное", "шопинг"],
    time: "долгое",
    budget: "дорого",
    category: "торговля"
  },
  {
    id: 13,
    name: "Государственная галерея им. А.А. Кадырова",
    imgs: [
      { url: "https://sun9-40.userapi.com/impg/YxwHHVR7wprIfdqIK5GVvJSi9LDOYVYJDudWcA/oIxrddp7nPs.jpg?size=604x340&quality=95&sign=49f50d4b5080496b95c26f68ba228f86&type=album", is_main: true },
      { url: "https://cdn.culture.ru/images/af6a6828-5df4-56c3-95a4-5816b272bab4", is_main: false },
      { url: "https://cdn.culture.ru/images/a8d6bfe8-144f-556a-aa06-8958551d6a7a", is_main: false }
    ],
    mood: ["культурное", "эстетическое"],
    time: "среднее",
    budget: "дешево",
    category: "искусство"
  },
  {
    id: 14,
    name: "Сквер Журналистов",
    imgs: [
      { url: "https://grozny.tv/storage/images/189b5c18-bdd2-45e6-a99d-bf43d40b99fb.jpg", is_main: true },
      { url: "https://avatars.mds.yandex.net/i?id=a8ef97866c972e5580e554c175feab6498853045-4869642-images-thumbs&n=13", is_main: false },
      { url: "https://grozmer.ru/images/content/b1dbe2dd877342ab1f97c0fedc51d694.jpg", is_main: false }
    ],
    mood: ["спокойное", "прогулочное"],
    time: "короткое",
    budget: "бесплатно",
    category: "город"
  },
  {
    id: 15,
    name: "Колизей в Грозном",
    imgs: [
      { url: "https://vestikavkaza.ru/upload/files3/colosseum-1.jpg", is_main: true },
      { url: "https://mayak.travel/m/picture/8/46/39/1240x520.21906a8e77ec8b4b077cc71648d7b06d1ed0d09864b014c13e746b05bc44704d.jpeg", is_main: false },
      { url: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Grozny_Koliseum_215.jpg/960px-Grozny_Koliseum_215.jpg", is_main: false }
    ],
    mood: ["развлекательное", "семейное"],
    time: "долгое",
    budget: "дешево",
    category: "развлечения"
  },
  {
    id: 16,
    name: "Бизнес-центр «Грозный Плаза»",
    imgs: [
      { url: "https://i.pinimg.com/736x/90/39/f3/9039f32001faca310c9acba1168f0d74.jpg", is_main: true },
      { url: "https://fototerra.ru/photo/Russia/Groznyj/large-292445.jpg", is_main: false },
      { url: "https://avatars.mds.yandex.net/i?id=e250193466ebbe12f85fd2da6cb819c9_l-5221376-images-thumbs&n=13", is_main: false }
    ],
    mood: ["деловое", "нейтральное"],
    time: "короткое",
    budget: "бесплатно",
    category: "архитектура"
  },
  {
    id: 17,
    name: "Парк Материнской Славы",
    imgs: [
      { url: "https://images.fooby.ru/1/77/54/3826712", is_main: true },
      { url: "https://georating.ru/img/photos/groznyy_1589371353.jpg", is_main: false },
      { url: "https://extraguide.ru/images/blog/2023/10-12-yjn9wz-park-materinskoy-slavy.jpeg", is_main: false }
    ],
    mood: ["семейное", "спокойное"],
    time: "среднее",
    budget: "бесплатно",
    category: "отдых"
  },
  {
    id: 18,
    name: "Чеченский государственный университет",
    imgs: [
      { url: "https://www.avanta55.ru/wp-content/uploads/2023/04/mebel-dlya-auditorij-v-groznom.jpg", is_main: true },
      { url: "https://grozny.tv/storage/images/7b8ac9d4d6746b69.jpeg", is_main: false },
      { url: "https://ivgpu.ru/images/gallery/20190120-ivanovskiy-politeh-rasshiryaet-gorizonty-sotrudnichestva/image2.jpeg", is_main: false }
    ],
    mood: ["познавательное", "нейтральное"],
    time: "короткое",
    budget: "бесплатно",
    category: "образование"
  },
  {
    id: 19,
    name: "Фонтанный комплекс на площади Дружбы",
    imgs: [
      { url: "https://sun9-7.userapi.com/impg/rt11dcs6XbdjgU6vf1LZI3Fj7HYP-A2vCIn0sw/Hb0RbjHYy_o.jpg?size=604x402&quality=96&sign=2655aba7aafda4a0be02ba6d20e2017d&type=album", is_main: true },
      { url: "https://oase-russia.ru/files/images/moskpl-1b.jpg", is_main: false },
      { url: "https://avatars.dzeninfra.ru/get-zen_doc/1881616/pub_64d9d451d79ed94465888813_64d9d4a8a14ed76cfb2b04f7/scale_1200", is_main: false }
    ],
    mood: ["романтическое", "вечернее"],
    time: "короткое",
    budget: "бесплатно",
    category: "город"
  },
  {
    id: 20,
    name: "Улица шашлыков",
    imgs: [
      { url: "https://avatars.dzeninfra.ru/get-zen_doc/1583391/pub_6119610c29330d3d3e7f7e00_61ed152e28232b76a3d59e79/scale_1200", is_main: true },
      { url: "https://avatars.dzeninfra.ru/get-zen_doc/4384151/pub_60d59c523712eb5540e8dac5_60dc6a254f502d1ca3f1cd24/scale_1200", is_main: false },
      { url: "https://psygazeta.ru/images/materialy/0-2024/may/18/m001.jpg", is_main: false }
    ],
    mood: ["гастрономическое", "национальное"],
    time: "среднее",
    budget: "дешево",
    category: "еда"
  },
  {
    id: 21,
    name: "Уличный кинотеатрЛетний кинотеатр под открытым небом на проспекте А.А. Кадырова",
    imgs: [
      { url: "https://static.mk.ru/upload/entities/2021/08/08/17/articlesImages/image/a6/f3/51/dd/cdf2847b9baa0a7ce082f2a6c3bcf0e6.jpg", is_main: true },
      { url: "https://www.grozny-inform.ru/LoadedImages/2023/05/11/WhatsApp_Image_2023-05-11_at_18.12.03_w900_h600.jpg", is_main: false },
      { url: "https://grozny-inform.ru/LoadedImages/2023/05/12/0883e08c-71a2-432e-90c7-ad8136d82e0a.jpg", is_main: false }
    ],
    mood: ["патриотическое", "историческое"],
    time: "среднее",
    budget: "бесплатно",
    category: "история"
  },
  {
    id: 22,
    name: "Сквер имени М.Ю. Лермонтова",
    imgs: [
      { url: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Бюст_Лермонтова_М.Ю._в_сквере_им._Лермонтова_М.Ю.jpg/1200px-Бюст_Лермонтова_М.Ю._в_сквере_им._Лермонтова_М.Ю.jpg", is_main: true },
      { url: "https://101квест.рф/upload/mediabiblioteka-blog/penza/skver-im-lermontova.webp", is_main: false },
      { url: "https://riapo.ru/upload/0penza/21/1156.jpg", is_main: false }
    ],
    mood: ["литературное", "спокойное"],
    time: "короткое",
    budget: "бесплатно",
    category: "город"
  },
  {
    id: 23,
    name: "Чеченский государственный театр юного зрителя",
    imgs: [
      { url: "", is_main: true },
      { url: "https://i.archi.ru/i/437455.jpg", is_main: false },
      { url: "https://i.archi.ru/i/437453.jpg", is_main: false }
    ],
    mood: ["семейное", "культурное"],
    time: "долгое",
    budget: "дешево",
    category: "театр"
  },
  {
    id: 24,
    name: "Грозненское водохранилище",
    imgs: [
      { url: "https://extraguide.ru/images/blog/2022/04-02-lajmrn-groznenskoe-more.png", is_main: true },
      { url: "https://avatars.dzeninfra.ru/get-zen_doc/1722013/pub_618fe4a77a99cb04b8b68e1e_618ff2cb65651d4aed836d80/scale_1200", is_main: false },
      { url: "https://avatars.mds.yandex.net/i?id=c77c660d0e6b33b1e0f686faeb6b40df_l-5228243-images-thumbs&n=13", is_main: false }
    ],
    mood: ["природное", "спокойное"],
    time: "долгое",
    budget: "бесплатно",
    category: "природа"
  }
];


export default activities