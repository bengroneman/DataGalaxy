import adapter from '@sveltejs/adapter-netlify';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	compilerOptions: {
		hydratable: true
	},
	kit: {
		adapter: adapter(),
		trailingSlash: 'always',
		prerender: {
			default: true
		}
	}
};

export default config;
