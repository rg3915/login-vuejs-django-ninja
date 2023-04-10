# Instalando TailwindCSS

[Documentação](https://tailwindcss.com/docs/installation)

```
yarn add tailwindcss
```

### Instale o [TailwindCSS](https://tailwindcss.com/) com Vite

[Install Tailwind CSS with Vite](https://tailwindcss.com/docs/guides/vite#vue)

```
npm i -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Edite `tailwind.config.js`

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx,vue}"
  ],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [],
}
```

```
touch src/style.css
```

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Instalando plugins e fontes

```
yarn add -D @tailwindcss/typography
```

[Poppings](https://blog.logrocket.com/how-to-use-custom-fonts-tailwind-css)

```js
/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: [
    "./public/**/*.html",
    "./src/**/*.{js,ts,vue}"
  ],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
        poppins: ['Poppins', 'sans-serif']
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
```

### Instalando forms

```
yarn add @tailwindcss/forms -D
```

```js
// tailwind.config.js
module.exports = {
  theme: {
    // ...
  },
  plugins: [
    require('@tailwindcss/forms'),
    // ...
  ],
}
```

### Instalando aspect-ratio

```
yarn add @tailwindcss/aspect-ratio
```

```js
// tailwind.config.js
module.exports = {
  theme: {
    // ...
  },
  corePlugins: {
    aspectRatio: false,
  },
  plugins: [
    require('@tailwindcss/aspect-ratio'),
    // ...
  ],
}
```

### Instalando Tailwind CSS Multi Theme

https://github.com/estevanmaito/tailwindcss-multi-theme#tailwind-css-multi-theme

```
yarn add tailwindcss-multi-theme
```

### [Prettier](https://prettier.io/) (Opcional)

```
yarn add --save-dev --save-exact prettier
```

```
echo {}> .prettierrc.json
```

```
cat << EOF > .prettierignore
# Ignore artifacts:
build
coverage
EOF
```

#### Rodando o Prettier

```
npx prettier --write public/
ou
yarn run lint
```
