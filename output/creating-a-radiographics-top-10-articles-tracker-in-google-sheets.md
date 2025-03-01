# Creating a Radiographics Top 10 Articles Tracker in Google Sheets

This guide walks you through the process of extracting article details from the Radiographics "Top 10 Articles" webpage and charting them in a Google Sheets spreadsheet. By following these steps, you will learn how to navigate the Radiographics website, extract details like title, authors, DOI, publication year, residency year, article level, and abstract, and then organize this data into a well-formatted and interactive Google Sheet.

---

## Step-by-Step Instructions

### 1. Navigate to the Radiographics Top 10 Articles Page

1. Open your web browser and go to [Google](https://www.google.com).
2. In the search bar, type **"Radiographics Top 10 Articles"**.
3. Locate and click on the first search result, typically labeled **"RG TEAM Top 10 Reading List"**.
4. Ensure that the page displays multiple categories of articles (e.g., Breast Imaging, Cardiac, Emergency, etc.).

### 2. Explore the Categories and Select an Article

1. Review the list of categories on the page, which are grouped by residency years and subdivided into levels (Basic, Intermediate, Advanced).
2. Click on one of the categories (for example, **Breast Imaging**).
3. Within the chosen category, select an article (e.g., from the Basic category for R1 residents).
4. **Tip:** After viewing an article, if you want to return to the main list of articles, click your browser's **Back** button.

### 3. Log into Google Drive

1. Open a new browser tab and navigate to [drive.google.com](https://drive.google.com).
2. Log in with your Google account. If you are prompted for credentials, use your personal or institutional credentials as applicable. Follow any on-screen instructions for two-factor authentication or passkey use.

### 4. Create a New Folder in Google Drive

1. In Google Drive, click on the **New** button in the upper left corner.
2. Select **Folder** from the dropdown menu.
3. Name the folder (e.g., **"RG-Top10-Articles"**) and click **Create**.
4. Open the newly created folder by double-clicking it.

### 5. Create and Set Up a Google Spreadsheet

1. Inside the folder, click the **New** button and select **Google Sheets** to create a blank spreadsheet.
2. Rename the spreadsheet to **"Top 10 Article Tracker"** by clicking on the title.
3. In the first row, set up the following column headers:
   - **Title**
   - **Author List**
   - **DOI**
   - **Year**
   - **R Year** (for residency year)
   - **Level**
   - **Abstract**

### 6. Format the Spreadsheet

1. **Adjusting the Layout:**
   - Resize columns as needed and delete any unnecessary columns to create a tidy workspace.
2. **Setting Up Data Validation (Dropdown Menus):**
   - For the **R Year** column:
     1. Select the cells under the header where you want a dropdown (e.g., B2:B if that column holds residency year data).
     2. Click on **Data** in the top menu and then select **Data Validation**.
     3. Under **Criteria**, choose **List of items** and type: `R1, R2, R3, R4`.
     4. Click **Save**.
   - For the **Level** column:
     1. Select the cells under the header where you want the level options.
     2. Go to **Data > Data Validation**.
     3. Under **Criteria**, choose **List of items** and type: `Basic, Intermediate, Advanced`.
     4. Click **Save**.
3. **Color Coding (Optional):**
   - You can assign colors to the dropdown items by selecting the cells and using the fill color option to visually differentiate between R Years or Levels.
4. **Text Wrapping:**
   - For columns that may have long text (like **Abstract**), select the column, click on the **Text wrapping** icon in the toolbar, and choose your preferred wrapping option.

### 7. Extract and Enter Article Data

For each article extracted from the Radiographics website, perform the following steps:

1. **Title:**
   - Copy the title from the Radiographics article page.
   - Paste it into the **Title** column of your spreadsheet.

2. **Author List:**
   - Copy the list of authors from the article page.
   - Instead of using unconventional methods to clear formatting, paste the text as plain text. You can do this by using the shortcut **Ctrl+Shift+V** (Windows) or **Cmd+Shift+V** (Mac) or by pasting it first into a plain text editor (like Notepad) and then copying it into the spreadsheet.
   - Paste the cleaned text into the **Author List** column.

3. **DOI:**
   - Copy the DOI link from the article page.
   - Paste it into the **DOI** column.

4. **Year:**
   - Enter the publication year as shown on the article page (e.g., `2019`) into the **Year** column.

5. **R Year:**
   - Based on the residency year indicated on the page (e.g., R1), select the corresponding option from the dropdown in the **R Year** column.

6. **Level:**
   - Identify the article level (Basic, Intermediate, Advanced) on the page and select it from the dropdown in the **Level** column. The dropdown should already reflect these options, ensuring consistency across entries.

7. **Abstract:**
   - Copy the abstract from the article page.
   - To remove any unwanted formatting, paste the abstract as plain text using **Ctrl+Shift+V** (Windows) or **Cmd+Shift+V** (Mac). Alternatively, paste it into a plain text editor (like Notepad) first, then copy and paste the cleaned text into the **Abstract** column.

### 8. Repeat for All Articles

1. After entering data for one article, return to the main list of articles by clicking your browser's **Back** button. This will help you navigate seamlessly between the article page and the list.
2. Repeat the data extraction and entry steps (as described in Section 7) for every article across all categories, residency years, and levels available on the Radiographics webpage.

### 9. Finalize and Beautify the Spreadsheet

1. Review the entire spreadsheet to ensure consistency and accuracy.
2. Apply additional formatting if desired (e.g., bold titles or adjust font sizes) to enhance visual clarity.
3. Remove any extra empty rows at the bottom of the spreadsheet.
4. Confirm that the dropdown menus and color coding are correctly applied. Your spreadsheet should now be clean, well-organized, and ready for further processing in your Python projects or other data applications.

---

## Summary

By following these steps, you have:

- Navigated to and explored the Radiographics Top 10 Articles webpage
- Extracted critical details (title, author list, DOI, publication year, residency year, level, and abstract) for each article
- Logged into Google Drive, created a dedicated folder, and set up a formatted Google Spreadsheet
- Applied data validation and formatting to ensure data integrity and visual appeal
- Entered the article data while using standard methods to eliminate unwanted text formatting
- Ensured smooth navigation between pages and consistency across all entries

Your final Google Sheet is now a comprehensive and well-organized tracker for Radiographics Top 10 articles, ready for further analysis or processing.

Happy charting!