/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        primary: 'rgb(38, 33, 37)',      // RGB(38, 33, 37)
        secondary: 'rgb(164, 127, 72)',   // RGB(164, 127, 72)
        text: 'rgb(101, 108, 116)',       // RGB(101, 108, 116)
        background: 'rgb(238, 237, 232)', // RGB(238, 237, 232)
      },
      fontFamily: {
        montserrat: ['Montserrat', 'sans-serif'],
        hind: ['Hind', 'sans-serif'],
      },
    },
  },
  plugins: [],
}