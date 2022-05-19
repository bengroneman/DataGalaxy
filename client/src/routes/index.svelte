<script>
	// helpers
	import { onMount } from 'svelte';
	import env from '../lib/env.js';

	// components
	import PreLoadImage from '../components/PreLoadImage.svelte';
	import NewImageForm from '../components/NewImageForm.svelte';
	import LoadingIcon from '../components/icons/LoadingIcon.svelte';
	import CategoryBreakdownChart from '../components/charts/CategoryBreakdownChart.svelte';
	import Modal from '../components/Modal.svelte';

	// globals
	let imagesAvailable = [];
	let modalOpen = false;
	let filename;
	let loading;
	$: imageSizesByCategory = imagesAvailable.map((image) => [image.size, image.category]);
	$: uniqueCategories = () => {
		let categories = imagesAvailable.map((image) => image.category);
		return [...new Set(categories)];
	}

	const BASE_URL = env.baseUrl;

	// lifecycle hooks
	onMount(async () => {
		await fetchAllImages();
	});

	// methods
	async function fetchAllImages() {
		loading = true;
		const response = await fetch(`${BASE_URL}api/images/`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			}
		});
		imagesAvailable = await response.json();
		loading = false;
	}
	const setNewImageModalOn = (imgId) => {
		modalOpen = true;
		filename = imagesAvailable.find((img) => img.id === imgId).filename;
	};
</script>

{#if modalOpen}
	<Modal on:close={() => (modalOpen = false)}>
		<NewImageForm bind:loading fetchAllImages={() => fetchAllImages()} />
	</Modal>
{/if}

<div class="text-center mt-12 pt-12">
	<svg
		class="mx-auto h-12 w-12 text-gray-400"
		fill="none"
		viewBox="0 0 24 24"
		stroke="currentColor"
		aria-hidden="true"
	>
		<path
			vector-effect="non-scaling-stroke"
			stroke-linecap="round"
			stroke-linejoin="round"
			stroke-width="2"
			d="M9 13h6m-3-3v6m-9 1V7a2 2 0 012-2h6l2 2h6a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2z"
		/>
	</svg>
	<h3 class="mt-2 text-md font-semibold text-gray-900">
		<span class="underline decoration-2 decoration-sky-500"
			>{imagesAvailable.length >= 1 ? imagesAvailable.length : 'No'}</span
		> images
	</h3>
	<p class="mt-1 text-sm text-gray-500">Get started by adding a new image.</p>
	<div class="mt-6">
		<button
			type="button"
			on:click={() => (modalOpen = true)}
			id="newImageButton"
			class="open-modal inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-orange-600 hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500"
		>
			<!-- Heroicon name: solid/plus -->
			<svg
				class="-ml-1 mr-2 h-5 w-5"
				xmlns="http://www.w3.org/2000/svg"
				viewBox="0 0 20 20"
				fill="currentColor"
				aria-hidden="true"
			>
				<path
					fill-rule="evenodd"
					d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z"
					clip-rule="evenodd"
				/>
			</svg>
			Add Image
		</button>
	</div>
	<div class="py-12 my-12">
		<h2 class="text-2xl mb-12">Images</h2>
		{#if loading}
			<span class="flex justify-center">
				<LoadingIcon />
			</span>
		{/if}
		<div id="imageGrid" class="grid lg:grid-cols-6 xl:grid-cols-8 md:grid-cols-4 sm:grid-cols-2">
			{#each imagesAvailable as image}
				<PreLoadImage bind:image />
			{/each}
		</div>
	</div>
	<div class="py-12 my-12">
		<h2 class="text-2xl mb-12 text-orange-400">Data breakdown</h2>
		<div class="grid lg:grid-cols-2 sm:grid-cols-1">
		</div>
	</div>
</div>
