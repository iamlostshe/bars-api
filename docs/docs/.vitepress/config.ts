export default {
  lang: 'en-US',
  title: 'bars-api',
  description: 'API-клиент, для взаимодействия с дневником.',
  sitemap: {
    hostname: 'https://bars-api.readthedocs.io'
  },
  themeConfig: {
    sidebar: [
      {
        items: [
          { text: "Быстрый старт", link: '/' },
          {
          text: 'Методы',
          items: [
              { text: 'get_birthdays', link: '/methods/get_birthdays.md' },
              { text: 'get_class_hours', link: '/methods/get_class_hours.md' },
              { text: 'get_class_year_info', link: '/methods/get_class_year_info.md' },
              { text: 'get_events', link: '/methods/get_events.md' },
              { text: 'get_person_data', link: '/methods/get_person_data.md' },
              { text: 'get_school_info', link: '/methods/get_school_info.md' },
              { text: 'get_summary_marks', link: '/methods/get_summary_marks.md' },
              { text: 'get_total_marks', link: '/methods/get_total_marks.md' },
            ]
          },
        ],
      },
    ]
  }
}
