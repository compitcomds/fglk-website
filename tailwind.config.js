/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["*"],
  theme: {
    extend: {
      // colors: {
      //   primary:"#fffbf7",
      //   secondaryp:"#fed1fa",
      //   secondaryo:"#fb6242",
      //   secondaryg: "#ceec87",
      //   button: "#e87b38",
      //   buttonhover: "#f8c23a",
      // },
      
      colors: {
        primary:"#fffbf7",
        secondaryp:"#fed1fa",
        secondaryo:"#fb6242",
        secondaryg: "#3fc446",
        button: "#e87b38",
        buttonhover: "#f8c23a",
        textcol : "#000000",
        white_back : "#ffff",
      },
      fontFamily: {
        
        webFont: ['Raleway', 'sans-serif'],

      },
      keyframes: {
        'background-animation': {
          '0%, 100%': { transform: 'rotate(0deg)' },
          '100%': { transform: 'rotate(360deg)' },
        },
      },
    },
    plugins: [],
  },
};