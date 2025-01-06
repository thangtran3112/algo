import globals from 'globals';
import pluginJs from '@eslint/js';
import tseslint from 'typescript-eslint';
import prettier from 'eslint-plugin-prettier';
import eslintConfigPrettier from 'eslint-config-prettier';

export default [
    { files: ['**/*.{js,mjs,cjs,ts}'] },
    { languageOptions: { globals: globals.browser } },
    pluginJs.configs.recommended,
    ...tseslint.configs.recommended,
    {
        files: ['tests/**/*'],
        languageOptions: {
            globals: {
                jest: true,
            },
        },
    },
    {
        plugins: {
            prettier: prettier,
        },
        rules: {
            'prettier/prettier': 'error',
            ...eslintConfigPrettier.rules,
        },
    },
];
