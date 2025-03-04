# Guide: Charting Radiographics Top 10 Articles into a Google Spreadsheet

This guide explains how to automatically chart and organize the top 10 Radiographics articles into a Google Spreadsheet. You will learn how to navigate the Radiographics website to extract details such as the article title, abstract, author list, DOI, publication year, residency year (R Year), and article level (e.g., Basic, Intermediate, Advanced). Once you have this information, you can enter it into a structured Google Sheet for later processing, such as using it in a Python project.

---

## Step 1: Navigate to the Radiographics Top 10 Articles Page

1. Open your web browser.
2. In the search bar, type "Radiographics top 10 articles" and press Enter.
3. From the Google search results, click on the link titled **RG TEAM Top 10 Reading List**.

```
[SCREENSHOT_PLACEHOLDER]
Name: search results
Purpose: Show the Google search results for "Radiographics top 10 articles"
Content: The browser window displaying the Google page with the returned search results, highlighting the RG TEAM Top 10 Reading List as the first result
Value: Helps identify the correct link for Radiographics articles
[/SCREENSHOT_PLACEHOLDER]

4. Once the page loads, you will see several categories (e.g., Breast Imaging, Cardiac, Emergency) each containing articles organized by residency years (R1, R2, etc.).

---

## Step 2: Select a Specific Category and Article

1. Zoom in on the page as needed for a clearer view of the categories.
2. Click on any category (for example, **Breast Imaging**) to reveal the available residency year lists and their corresponding articles.
3. Choose an article from one of the residency year groups (e.g., for Resident Year 1, select an article like "Digital Breast Tomosynthesis: Physics, Artifacts, and Quality Control Considerations").

```
[SCREENSHOT_PLACEHOLDER]
Name: article page
Purpose: Show the selected article page within a chosen category on the Radiographics website
Content: The browser window displaying the detailed page of a Radiographics article with its title, abstract, DOI, authors, and other details
Value: Serves as a visual reference for gathering article details
[/SCREENSHOT_PLACEHOLDER]

4. **Returning to Main List:** After extracting the necessary information from an article, use your browser's back button or reopen the Radiographics Top 10 Reading List in a new tab so you can continue processing the next article.

---

## Step 3: Sign in to Google Drive and Create a New Folder

1. Open a new browser tab and navigate to [drive.google.com](https://drive.google.com/).
2. Sign into your Google account. (Note: If you see a different login prompt or are using an alternate account, follow the onscreen instructions to log in.)

```
[SCREENSHOT_PLACEHOLDER]
Name: google drive
Purpose: Demonstrate the Google Drive login page
Content: The Google Drive homepage with the account selected and options visible
Value: Confirms that the user is logged into their Google Drive before proceeding
[/SCREENSHOT_PLACEHOLDER]

3. In Google Drive, create a new folder:
   - Right-click on an empty area of your drive and select **New folder**.
   - Name the folder `RG-Top10-Articles`.
   - Click **Create**.

```
[SCREENSHOT_PLACEHOLDER]
Name: new folder
Purpose: Show how to create and name a folder in Google Drive
Content: A screenshot of the right-click context menu with the 'New folder' option highlighted and the dialog box for naming the folder
Value: Visual guidance for correctly setting up the workspace in Google Drive
[/SCREENSHOT_PLACEHOLDER]

4. Open the newly created `RG-Top10-Articles` folder.

---

## Step 4: Create and Set Up a New Google Spreadsheet

1. Within your new folder, click the **+ New** button and select **Google Sheets** → **Blank spreadsheet**.
2. Once the spreadsheet opens, rename it to `Top 10 Articles`.
3. Set up the table by creating the following column headers, where each row will represent a single article:
   - Title
   - Author List
   - DOI
   - Year
   - R Year (Residency Year)
   - Level
   - Abstract
4. To keep the spreadsheet neat, delete any extra columns (e.g., columns G to Z):
   - Click on the column header (e.g., G), right-click, and choose **Delete column**. Repeat this for each extra column.

---

## Step 5: Configure Drop-Down Menus for the 'Level' and 'R Year' Columns

1. For the **Level** column:
   - Select the cells you want to restrict (or click the column header).
   - Go to **Data** > **Data validation** in the menu.
   - Select **List of items** and enter: `Basic, Intermediate, Advanced`.
   - (Optionally) Use cell formatting to assign different colors for visual appeal.

2. For the **R Year** column:
   - Similarly, set up a drop-down menu with the options: `R1, R2, R3, R4`.
   - (Optionally) adjust the formatting of these cells to improve visibility.

```
[SCREENSHOT_PLACEHOLDER]
Name: dropdown setup
Purpose: Illustrate the creation of drop-down menus in Google Sheets
Content: The Google Sheets data validation window showing drop-down options defined for either the Level or R Year column
Value: Aids users in configuring the spreadsheet to maintain consistency when entering data
[/SCREENSHOT_PLACEHOLDER]

---

## Step 6: Populate the Spreadsheet with Article Data

For each article in the Radiographics Top 10 list, follow these detailed sub-steps:

1. **Copy the Article Title:**
   - Highlight and copy the title from the Radiographics article page.
   - Paste it into the `Title` column of the Google Sheet.

2. **Extract and Clean the Abstract:**
   - Highlight and copy the abstract text from the article page.
   - **Optional Cleaning Step:** Paste the abstract into your browser's address bar (or an alternative plain text editor such as Notepad) to remove any extra formatting or unwanted line breaks. Then, copy the cleaned text and paste it into the `Abstract` column. 
   - **Rationale:** This step helps ensure that the text is free from unusual characters or formatting that might cause issues in later data processing.

3. **Copy and Clean the Author List:**
   - Highlight and copy the author list from the article page.
   - Use the same cleaning method (pasting into the browser's address bar or Notepad), then copy and paste the clean text into the `Author List` column.

4. **Extract and Enter the DOI:**
   - Highlight and copy the DOI (link) from the article page.
   - Paste the DOI into the `DOI` column of the spreadsheet.

5. **Enter the Year:**
   - Manually type the publication year (for example, `2019`) into the `Year` column.

6. **Select the Residency Year:**
   - In the `R Year` column, choose the appropriate residency year (e.g., `R1`) from the drop-down menu.

7. **Select the Article Level:**
   - In the `Level` column, choose the corresponding level (e.g., `Basic`) from the drop-down menu.

```
[SCREENSHOT_PLACEHOLDER]
Name: data entry
Purpose: Show a fully populated row with article details
Content: Google Sheet row with Title, Abstract (truncated for visibility), Author List, DOI, Year, R Year, and Level all filled in
Value: Confirms correct data formatting and placement for each article entry
[/SCREENSHOT_PLACEHOLDER]

8. Repeat the above sub-steps for each article in the list.

---

## Step 7: Finalize and Beautify the Spreadsheet

1. After entering data for all articles, review the spreadsheet to ensure no extra rows or columns remain.
2. Delete any unnecessary rows or columns (e.g., any extra columns beyond the defined headers) by right-clicking on the column header and selecting **Delete column**.
3. Enhance the spreadsheet's visual appeal by:
   - Bolding the header row
   - Adjusting column widths for readability
   - Formatting cells to ensure text is aligned and wrapped as necessary

```
[SCREENSHOT_PLACEHOLDER]
Name: final layout
Purpose: Display the complete, formatted spreadsheet
Content: Full spreadsheet view with all columns neatly aligned, headers bolded, and drop-down menus visible
Value: Provides a reference for final structure and formatting expectations
[/SCREENSHOT_PLACEHOLDER]

4. Once completed, notify yourself (or your team) that the Google Spreadsheet is fully prepared for further processing using your Python script or other applications.

---

## Conclusion

You have now learned how to chart Radiographics' Top 10 Articles into a Google Spreadsheet. This process includes navigating the website, extracting and cleaning data, and setting up a clearly formatted and consistent spreadsheet for future use. Follow each step carefully—especially the data cleaning and navigation steps—to ensure smooth, error-free data collection.

Happy charting!