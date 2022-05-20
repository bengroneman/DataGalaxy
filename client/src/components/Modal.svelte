<script>
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();
	const close = async () => dispatch('close');

	let modal;

	const handleKeyDown = (e) => {
		if (e.key === 'Escape') {
			close();
		}
	};
</script>

<svelte:window on:keydown={handleKeyDown} />
<div
	id="newImageModal"
	class="relative z-10"
	aria-labelledby="new image modal"
	role="dialog"
	bind:this={modal}
	aria-modal="true"
>
	<div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />

	<div class="fixed z-10 inset-0 overflow-y-auto">
		<div class="flex items-end sm:items-center justify-center min-h-full p-4 text-center sm:p-0">
			<div
				class="bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:max-w-fit sm:w-full sm:p-6"
			>
				<div class="mt-3 text-center sm:mt-5">
					<slot />
					<button
						type="button"
						on:click={() => close()}
						class="cancel-modal mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-orange-500 sm:mt-0 sm:col-start-1 sm:text-sm"
						>Cancel</button
					>
				</div>
			</div>
		</div>
	</div>
</div>
