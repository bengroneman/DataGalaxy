import { expect, test } from '@playwright/test';

test('adding a PNG is successful', async ({ page, request }) => {
	page.on('load', async () => {
		await page.locator('button.open-modal').click();
		await page.locator('label.input-file');
		page.on('filechooser', async (fileChooser) => {
			await fileChooser.setFiles('../assets/100x400.png');
		});

		await page.locator('#newImageForm .save-image').click();
		expect(await request.response.status).toBe(200);
	});
});

test('adding a PDF fails', async ({ page, request }) => {
	page.on('load', async () => {
		await page.locator('button.open-modal').click();
		await page.locator('label.input-file');
		page.on('filechooser', async (fileChooser) => {
			await fileChooser.setFiles('../assets/Portfolio.pdf');
		});

		await page.locator('#newImageForm .save-image').click();
		expect(await request.response.status).toBe(400);
	});
});

test('adding a file over 10mb fails', async ({ page, request }) => {
	page.on('load', async () => {
		await page.locator('button.open-modal').click();
		await page.locator('label.input-file');
		page.on('filechooser', async (fileChooser) => {
			await fileChooser.setFiles('../assets/10mb.png');
		});

		await page.locator('#newImageForm .save-image').click();
		expect(await request.response.status).toBe(400);
	});
});
