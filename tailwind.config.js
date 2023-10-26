/** @type {import('tailwindcss').Config} */
module.exports = {
  prefix: 'tw-', 
  corePlugins: {
    preflight:false, 
  }, 
  content: ["./core/templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors:{
        'theme-1': '#2F80ED', 
        'theme-2': '#9B51E0', 
        'theme-3':'#ED9B2F', 
        'theme-4':'#335F3E',
      }
    },
  },
  plugins: [],
}

// npx tailwindcss -i ./core/static/css/tailwindcss/input.css -o ./core/static/css/tailwindcss/dist/output.css --watch