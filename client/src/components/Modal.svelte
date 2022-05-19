<div
    id="newImageModal"
    class="relative z-10"
    aria-labelledby="new image modal"
    role="dialog"
    aria-modal="true"
>
    <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />

    <div class="fixed z-10 inset-0 overflow-y-auto">
        <div class="flex items-end sm:items-center justify-center min-h-full p-4 text-center sm:p-0">
            <div class="bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:max-w-lg sm:w-full sm:p-6">
                <div class="mt-3 text-center sm:mt-5">
                    <slot />
                </div>
            </div>
        </div>
    </div>
</div>