<script>
	// helpers
	import env from '../lib/env.js';

	// components
	import CategoryFilter from '../components/CategoryFilter.svelte';

	// globals
	$: selectedCategory = 'General';
	const BASE_URL = env.baseUrl;

	// props
	export let fetchAllImages = () => {};
	export let loading;
	let image;
	const categories = ['Cats', 'Dogs', 'General', 'Stock', 'Projects', 'Technology'];

	// functions
	function closeModal() {
		document.querySelector('#image').value = '';
	}
	async function handleSubmit() {
		loading = true;
		event.preventDefault();
		const form = this;
		const data = new FormData(form);

		if (document.querySelector('#image').value === '') {
			alert('Please attach an image');
			return;
		}
		const response = await fetch(`${BASE_URL}api/images/`, {
			method: 'POST',
			body: data
		});

		const parsed_response = await response.json();
		if (parsed_response.hasOwnProperty('error')) {
			alert(parsed_response.error);
			loading = false;
		} else {
			const input = document.querySelector('#image');
			input.value = '';
			await fetchAllImages();
			loading = false;
			alert('Image uploaded successfully');
		}
	}
</script>

<form class="new-image-form" name="newImageForm" id="newImageForm" on:submit={handleSubmit}>
	<input type="hidden" name="category" bind:value={selectedCategory} />
	<div class="space-y-8 divide-y divide-gray-200">
		<div>
			<div>
				<h3 class="text-lg leading-6 font-medium text-gray-900">Add a new image</h3>
				<p class="mt-1 text-sm text-gray-500">
					This image will be displayed publicly so be careful what you share.
				</p>
			</div>

			<div class="divide-y divide-gray-200 h-full">
				<CategoryFilter
					label="Categories"
					options={categories}
					bind:selectedOption={selectedCategory}
				/>
			</div>

			<div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
				<div class="sm:col-span-6">
					<div
						class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md"
					>
						<div class="space-y-1 text-center">
							<svg
								class="mx-auto h-12 w-12 text-gray-400"
								stroke="currentColor"
								fill="none"
								viewBox="0 0 48 48"
								aria-hidden="true"
							>
								<path
									d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
							<div class="flex text-sm text-gray-600">
								<label
									for="image"
									class="file-input relative cursor-pointer bg-white rounded-md font-medium text-orange-600 hover:text-orange-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-orange-500"
								>
									<input id="image" name="image" type="file" class="px-2" />
								</label>
							</div>
							<p class="text-xs text-gray-500">PNG, JPG, GIF up to 10MB</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

	<button
		type="submit"
		class="save-image my-6 w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-orange-600 text-base font-medium text-white hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500 sm:col-start-2 sm:text-sm"
		>Save</button
	>
</form>
