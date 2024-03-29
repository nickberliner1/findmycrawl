export default {
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'findmycrawl-frontend',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
  ],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    ['nuxt-fontawesome', {
      component: 'fa',
      imports: [{
        set: '@fortawesome/free-solid-svg-icons',
        icons: ['faLightbulb']
        },
        {set: '@fortawesome/free-brands-svg-icons',
        icons: ['faGithub']
        },
        {set: '@fortawesome/free-regular-svg-icons',
        icons: ['faLightbulb']
        },
        {
          set: '@fortawesome/free-solid-svg-icons',
          icons: ['faArrowLeft']
        }]
    }]
  ],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // https://go.nuxtjs.dev/bootstrap
    'bootstrap-vue/nuxt',
    '@nuxtjs/axios',
    '@nuxtjs/sitemap'
  ],

  // axios: {
  //   baseURL: 'http://localhost/8000/api'
  // },

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
  }
}
