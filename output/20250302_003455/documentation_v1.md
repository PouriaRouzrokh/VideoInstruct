# How to Chart RadioGraphics Top 10 Articles in Google Sheets

This guide explains how to automatically chart articles from the RadioGraphics Top 10 reading list into a Google Sheets spreadsheet. By following these steps, you will duplicate the process demonstrated in the video, from accessing the website to formatting your spreadsheet for further analysis.

## Introduction

In this guide, you will learn how to:

- Navigate to the RadioGraphics Top 10 articles page using a web search.
- Select a subspecialty (e.g., Breast Imaging or Cardiac) and a particular article category (e.g., Basic, Intermediate, Advanced).
- Extract key information from an article page, such as the title, author list, publication year, DOI, abstract, etc.
- Log into Google Drive, create a dedicated folder, and set up a new Google Sheet to store the article data.
- Format the spreadsheet by creating specific columns, using data validation for dropdown menus, cleaning up pasted text, and applying a clean design.

Follow this step-by-step guide to build your own chart automatically.

## Step-by-Step Instructions

### 1. Navigate to the RadioGraphics Top 10 Articles Page

1. Open your preferred web browser (the video example uses Arc).
2. In the browser's address bar, type "radiographics top 10 articles" and hit Enter.
3. In the search results, look for the link titled **RG TEAM Top 10 reading list** and click on it.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show Google search results for "radiographics top 10 articles"
Content: The browser window with the search results highlighted, specifically the "RG TEAM Top 10 reading list" link
Value: Helps the user identify and click on the correct search result
[/SCREENSHOT_PLACEHOLDER]

```

### 2. Select a Subspecialty and Article Category

1. Once on the RadioGraphics website, you will see a list of subspecialties such as Breast Imaging, Cardiac, etc.
2. Zoom in if necessary to clearly view all the categories.
3. Click on one of the options (for example, "Breast Imaging").
4. Note that articles are organized further by Resident Year (R1, R2, etc.) and by category levels (e.g., Basic, Intermediate, Advanced).

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Display the RadioGraphics Top 10 page with subspecialty categories
Content: Screen view showing the various categories and residency years available
Value: Assists users in identifying which category to select
[/SCREENSHOT_PLACEHOLDER]

```

### 3. Open an Article Page

1. Click on an article (for example, a paper listed under the "Basic" category for R1 residents).
2. The article page will load. Note that you might not have full access to the article content, but key details (title, author list, abstract, DOI, year) will be available.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Illustrate an open article page with key details in view
Content: Webpage showing the article title, authors, abstract, etc., as seen on the RadioGraphics site
Value: Helps the user confirm they have selected an article correctly
[/SCREENSHOT_PLACEHOLDER]

```

### 4. Log Into Google Drive and Create a New Folder

1. Open a new browser tab and go to [drive.google.com](https://drive.google.com).
2. If you are not already logged into your Google account, use your appropriate login method (this might involve typing your email or using a passkey). Note: The login prompt may differ depending on your computer.
3. Once logged in, click the **+ New** button and select **New folder**.
4. Name the folder (e.g., `RG-Top10-Articles`) and create it.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Display the process of creating a new folder in Google Drive
Content: Google Drive interface with the new folder dialog open and a folder named "RG-Top10-Articles"
Value: Provides clarity on where to store your spreadsheet
[/SCREENSHOT_PLACEHOLDER]

```

### 5. Create and Name a New Google Sheet

1. Open your newly created folder by clicking on it.
2. Click the **+ New** button again, choose **Google Sheets**, and then select **Blank spreadsheet**.
3. Name the spreadsheet (e.g., `Top 10 Articles`).

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show the process of creating and naming a new Google Sheets file
Content: A blank spreadsheet open in Google Sheets with the custom name visible
Value: Ensures the user creates their workspace correctly
[/SCREENSHOT_PLACEHOLDER]

```

### 6. Set Up Spreadsheet Columns and Data Validation

1. In the first row of the Google Sheet, enter the following column headers:
   - **Column A:** Abstract
   - **Column B:** Author List
   - **Column C:** Year
   - **Column D:** DOI
   - **Column E:** R Year
   - **Column F:** Level

2. **Configure the "Level" Column:**
   - Select the entire column F (or the header cell) and click on **Data > Data validation**.
   - Change the criteria to **Dropdown** and add the following items one-by-one: `Basic`, `Intermediate`, `Advanced`.
   - Optionally, assign a distinct color to each option.
   - Click **Done**.

3. **Configure the "R Year" Column:**
   - Select column E and navigate to **Data > Data validation**.
   - Change the criteria to **Dropdown** and add items such as: `R1`, `R2`, `R3`, `R4` (or as required).
   - Optionally, assign colors to these options.
   - Click **Done**.

4. (Optional) Remove unnecessary default columns by selecting columns G to Z, right-clicking, and choosing **Delete columns**.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Demonstrate setting up column headers and dropdown menus with data validation
Content: Google Sheet with headers and an open Data Validation dialog showing the dropdown options add process
Value: Helps users replicate the exact dropdown settings for consistent data entry
[/SCREENSHOT_PLACEHOLDER]

```

### 7. Transfer Data for Each Article into the Spreadsheet

For each article on the RadioGraphics page, follow these steps:

1. **Split Your Screen:** Arrange the browser window so you can view both the RadioGraphics article page and the Google Sheet side by side.

2. **Extract and Paste Data:**
   - **Title:** Copy the article title and paste it into the appropriate cell in your spreadsheet.
   - **Author List:** Highlight and copy the list of authors. To ensure clean text without extra characters, paste the text into your browser's address bar first, then copy it again and paste it into the corresponding cell.
   - **Publication Year:** Manually enter the publication year (e.g., `2019`) into the Year column.
   - **DOI:** Copy the DOI link from the article page and paste it into the DOI column.
   - **R Year and Level:** Use the dropdown menus in the respective cells to select the appropriate Resident Year (e.g., `R1`) and Level (e.g., `Basic`).
   - **Abstract:** Copy the article abstract. If the abstract contains unwanted line breaks or extra spaces, paste it into the address bar to strip formatting, then copy it from there and paste it into the Abstract cell. Adjust text wrapping settings as needed.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show side-by-side view of an article page and the filled-out spreadsheet
Content: Left half displaying the Google Sheets with one row partially filled and the right half showing the article page in the browser
Value: Reduces ambiguity by demonstrating exactly what each pasted piece of text should look like
[/SCREENSHOT_PLACEHOLDER]

```

3. **Formatting:**
   - Bold any key text such as article titles for better readability.
   - Apply alternate colors to rows for better visual segmentation by selecting all relevant rows and clicking on **Format > Alternate colors**.
   - Remove any extra rows beyond those with data to maintain a clean layout.

### 8. Repeat the Process for All Articles

- Go back to the list of articles. For every category, residency year, and level available, repeat Step 7 until all articles are indexed in your spreadsheet.

```
[SCREENSHOT_PLACEHOLDER]
Purpose: Show a complete spreadsheet after data entry for multiple articles
Content: Full Google Sheet view with several rows filled in, clear dropdown selections, and an alternating color format applied
Value: Provides users with a final visual reference of how the finished document should look
[/SCREENSHOT_PLACEHOLDER]

```

### 9. Finalize and Save Your Spreadsheet

1. Once you have entered data for all articles, review the spreadsheet to ensure all data is correctly placed and formatted.
2. Delete any extra rows and columns that are not needed.
3. Save your changes. Your Google Sheet is now ready to be used in your Python scripts or other applications.
4. Notify your users or stakeholders that the spreadsheet creation process is complete.

## Conclusion

You have now successfully set up a workflow for automatically charting RadioGraphics Top 10 articles into a Google Sheet. This organized approach allows for easy import into programs like Python for further data processing and analysis. Follow these steps for every article category and residency year to maintain a neat and comprehensive dataset.

Happy charting!