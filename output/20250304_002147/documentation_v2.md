# Automating the Charting of Radiographics Top 10 Articles into a Google Spreadsheet

This guide details how to automatically chart Radiographics' top 10 articles from their website into a Google Spreadsheet. By following these steps, you will learn how to navigate the Radiographics website, extract key article information, set up your Google Drive workspace, and populate the spreadsheet with formatted data for further processing in Python or other applications.

---

## Introduction

In this guide, you will:

- Search for and navigate to the Radiographics top 10 articles page.
- Select a category (e.g., Breast Imaging, Cardiac) to view a list of articles specific to residency years.
- Extract details such as the article title, author list, publication year, DOI link, and abstract from each article (with a technique to remove extra formatting from abstracts).
- Log in to Google Drive, create a dedicated folder, and set up a new Google Sheets spreadsheet.
- Configure the spreadsheet with appropriate headers, dropdown menus (using Data Validation), and text wrapping to improve readability.

**Handling Multiple Categories:**

If you wish to chart articles from multiple categories (e.g., Breast Imaging, Cardiac, etc.), you have two options:

1. Create separate tabs within the same Google Spreadsheet for each category.
2. Add an additional column to denote the article category and keep all data in a single sheet.

Choose the approach that best suits your workflow and data analysis needs.

---

## Step-by-Step Instructions

### 1. Navigate to the Radiographics Top 10 Articles Page

1. Open your preferred web browser.
2. In the search bar, type "Radiographics top 10 articles" and press Enter.
3. Look through the search results and click on the link labeled **RG TEAM Top 10 Reading List** (this is the official page with all the categorized articles).

[SCREENSHOT_PLACEHOLDER]
Name: Radiographics Search
Purpose: Show the Google search interface with the query "Radiographics top 10 articles" and highlight the RG TEAM link.
Content: A browser window displaying the Google search results with the top result labeled "RG TEAM Top 10 Reading List".
Value: Helps users correctly identify and click the right link from the search results.
[/SCREENSHOT_PLACEHOLDER]

4. Once the page loads, adjust your view (using zoom if necessary) to clearly see the different categories and residency years (e.g., Breast Imaging, Cardiac, etc.).

[SCREENSHOT_PLACEHOLDER]
Name: Radiographics Page
Purpose: Illustrate the layout of the Radiographics top 10 articles page with visible categories.
Content: The full page displaying sections for different subspecialties and residency levels.
Value: Helps users locate article categories easily on the page.
[/SCREENSHOT_PLACEHOLDER]

---

### 2. Selecting an Article Category and Viewing Article Details

1. Click on any article category (for example, **Breast Imaging**).
2. The page will display articles arranged by residency year and categorized by levels (e.g., Basic, Intermediate, Advanced).
3. Click on an individual article (for example, one from the Basic category for R1 residents) to view its details.
4. On the article page, note the following information that you will record:
   - **Title** of the article
   - **Authors** (author list)
   - **Publication Year** (e.g., 2019)
   - **DOI URL** (copy the hyperlink as is)
   - **Abstract** (see Step 5.2 for cleaning the abstract text)
   - **Residency Year (R1, R2, etc.)** and **Article Level (Basic, Intermediate, Advanced)**

[SCREENSHOT_PLACEHOLDER]
Name: Article Details
Purpose: Show an example article page with highlighted areas for the title, author list, and DOI.
Content: A browser view of an article with annotations indicating where to find the title, author list, year, DOI, and abstract.
Value: Provides clarity on how to extract the required data fields from each article page.
[/SCREENSHOT_PLACEHOLDER]

---

### 3. Setting Up Your Google Drive Workspace

1. Open a new browser tab and go to [https://drive.google.com](https://drive.google.com).
2. Ensure you are logged in using your desired Google account. If prompted, follow the on-screen instructions to log in or switch accounts.

[SCREENSHOT_PLACEHOLDER]
Name: Drive Dashboard
Purpose: Display the main Google Drive interface after login.
Content: A screenshot of the Google Drive homepage showing files and folders.
Value: Confirms you are in the correct environment to create new files.
[/SCREENSHOT_PLACEHOLDER]

3. Click on the **New** button and choose **Folder**.
4. Name the folder `RG-Top10-Articles`.
5. Open the newly created folder by double-clicking on it.
6. Inside the folder, click on **New** and then select **Google Sheets** to create a new blank spreadsheet.
7. Name the spreadsheet `Top 10 Articles`.

[SCREENSHOT_PLACEHOLDER]
Name: Sheet Setup
Purpose: Illustrate the process of creating a new Google Sheets file inside the project folder.
Content: The Google Sheets interface with the file title "Top 10 Articles" visible at the top.
Value: Guides users on where and how to create the spreadsheet needed for data entry.
[/SCREENSHOT_PLACEHOLDER]

---

### 4. Configuring the Spreadsheet

1. In the first row of the spreadsheet, create the following header columns (suggested order):
   - Title
   - Author List
   - Year
   - DOI
   - R Year
   - Level
   - Abstract

2. Format each header cell as bold for emphasis.
3. Adjust the width of each column to ensure the content is clearly visible.

4. *Creating Dropdown Menus for R Year and Level:*
   - Click the column header for **R Year** (or select the range of cells in that column).
   - Go to the top menu and click **Data** > **Data validation**.
   - Under **Criteria**, choose **List of items** and enter: `R1,R2,R3,R4`.
   - Click **Save** to apply the dropdown.

   - Repeat the process for the **Level** column:
     - Select the **Level** column cells.
     - Click **Data** > **Data validation**.
     - Under **Criteria**, choose **List of items** and enter: `Basic,Intermediate,Advanced`.
     - Click **Save**.

[SCREENSHOT_PLACEHOLDER]
Name: Data Validation
Purpose: Show the Google Sheets Data Validation dialog for dropdown creation with sample values entered.
Content: The Data Validation dialog box open with "List of items" selected and the fields populated with `Basic,Intermediate,Advanced` for the Level column.
Value: Helps users correctly configure dropdown menus for consistent data entry.
[/SCREENSHOT_PLACEHOLDER]

---

### 5. Populating the Spreadsheet with Article Data

For **each article** from the Radiographics page, perform the following steps:

1. **Extract and Record the Title**
   - Copy the title of the article from the article page and paste it into the appropriate cell under the *Title* column.

2. **Extract and Record the Author List**
   - Copy the author list from the article page. If you notice extra spaces or line breaks, use the cleaning technique described in Step 5.2 before pasting into the *Author List* column.

3. **Extract and Record the Publication Year**
   - Manually type or copy the publication year (e.g., 2019) into the *Year* column.

4. **Extract and Record the DOI Link**
   - Copy the DOI link from the article page and paste it into the *DOI* column. Ensure the link remains clickable.

5. **Set the Residency Year and Level**
   - In the *R Year* column, select the appropriate residency year (e.g., R1) from the dropdown list you configured.
   - In the *Level* column, select the corresponding article level (e.g., Basic, Intermediate, Advanced) from the dropdown.

6. **Extract and Record the Abstract**
   - Copy the article abstract from the page. Since pasting directly may include extra formatting (such as unnecessary line breaks and special characters), use the following text-cleaning method:
     1. Open a new tab in your browser.
     2. Click in the address bar and paste the copied abstract text. The address bar typically displays plain text without extra formatting.
     3. Highlight and copy the cleaned abstract text from the address bar.
     4. Paste the cleaned text into the *Abstract* column.

[SCREENSHOT_PLACEHOLDER]
Name: AddressBar Cleaning
Purpose: Demonstrate the text-cleaning process using the browser address bar to remove extra abstract formatting.
Content: A screenshot showing the abstract pasted in the browser address bar with cleaned text ready for re-copying.
Value: Aids users in understanding and replicating the text cleaning process to ensure clean data entry.
[/SCREENSHOT_PLACEHOLDER]

7. Repeat steps 1 through 6 for every article listed on the Radiographics page. If you are processing multiple categories, ensure you either create separate tabs for each category or include an extra column to indicate the article category.

---

### 6. Final Spreadsheet Touches

1. Once all articles have been charted, remove or delete any extra empty rows to keep the spreadsheet tidy.
2. Double-check the spreadsheet for consistency:
   - Ensure that all cells are visually aligned and formatted uniformly.
   - Confirm that dropdown menus for *R Year* and *Level* are correctly applied across all rows.
   - Verify that text wrapping is enabled (or disabled) as you prefer, particularly for the *Abstract* column.
3. Optionally, apply further cell formatting (e.g., bolding the titles or applying background colors) to enhance the visual appeal of the spreadsheet.
4. Save your changes. Your Google Spreadsheet is now neatly organized and ready for further processing in your Python projects or other applications.

---

## Conclusion

By following this guide, you have successfully navigated the Radiographics website, extracted key details for the top 10 articles, and organized all the information in a structured Google Spreadsheet. This setup not only streamlines manual data entry but also prepares the data for automation, analysis, and integration into future projects.

Happy charting!