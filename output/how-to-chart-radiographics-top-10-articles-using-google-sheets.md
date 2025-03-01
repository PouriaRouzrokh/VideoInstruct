# How to Chart Radiographics Top 10 Articles Using Google Sheets

This guide explains how to extract and organize information from Radiographics’ Top 10 Articles page into a Google Sheets spreadsheet. You will create a structured spreadsheet containing details for each article—Title, Author List, Abstract, DOI, Year, Resident Year, and Level. The guide also includes methods for cleaning text and setting up drop-down lists using Google Sheets' Data Validation feature.

---

## Introduction

The process involves three main parts:

1. Accessing the Radiographics Top 10 Articles page and selecting a category.
2. Creating and setting up a Google Sheets spreadsheet in Google Drive.
3. Extracting and entering article data into the spreadsheet using clean paste methods and Data Validation drop-downs.

_Note: If you need to work with articles from multiple categories, you may choose to either create separate sheets/tabs within the same spreadsheet for each category, or consolidate all data into one sheet with an additional column indicating the article category._

---

## Step-by-Step Instructions

### 1. Access the Radiographics Top 10 Articles Page

1. **Open Your Browser and Search**
   - Open a new browser window and go to Google.
   - Enter the search query "Radiographics top 10 articles".
   - Click on the first result (commonly labeled "RG TEAM Top 10 reading list").

2. **Browse the Page**
   - The page displays a list of subspecialties (e.g., Breast Imaging, Cardiac).
   - Articles are organized by residency year (e.g., R1, R2, etc.) and by level (e.g., Basic, Intermediate, Advanced).
   - Choose a subspecialty (e.g., click on Breast Imaging) to view the articles in that category.
   - Decide if you want to work with multiple categories. For each category, you may create separate tabs or include a column labeled "Category" in your consolidated sheet.


### 2. Prepare Google Drive and Create a Google Sheets Spreadsheet

1. **Log in to Google Drive**
   - Open a new browser tab and navigate to `https://drive.google.com`.
   - Ensure you are logged in. If not, sign in with your account. (If you need to switch accounts, sign out or use incognito mode.)

2. **Create a New Folder**
   - Click the "New" button and select "Folder".
   - Name the folder `RG-Top10-Articles` (or a preferred name) and open it.

3. **Create a New Google Sheets Spreadsheet**
   - Inside your new folder, click on the "New" button, then select "Google Sheets" > "Blank spreadsheet".
   - Name the spreadsheet `Top Ten Articles`.


### 3. Set Up the Spreadsheet

1. **Create Column Headers**
   - In the first row, create the following columns:
     - Title
     - Author List
     - Abstract
     - DOI
     - Year
     - R Year
     - Level
     - *(Optional: Category – if consolidating multiple categories)*

2. **Set Up Data Cleaning for Text Input**
   - **Use Paste Special (Unformatted Text):**
     - When copying text from the Radiographics website (for Title, Author List, and Abstract), use `Ctrl+Shift+V` (Windows) or `Command+Shift+V` (Mac) to paste the text without formatting.
     - Alternatively, in Google Sheets, right-click on a cell and choose **Paste values only** if you are copying from another Google Docs or similar source.

3. **Configure Text Wrapping**
   - Select all cells (click the top left corner of the sheet).
   - Go to the toolbar, click the text wrapping button, and choose **Wrap** (or refer to [Google Sheets text wrapping documentation](https://support.google.com/docs/answer/179738) for more details).

4. **Create Drop-Down Lists Using Data Validation**

   #### For the "Level" Column:
   1. Select the cells under the "Level" header (for example, starting from cell G2 to G100).
   2. Click on **Data** in the menu, then select **Data validation**.
   3. Under **Criteria**, select **List of items** and enter: `Basic, Intermediate, Advanced`.
   4. (Optional) Check the option to **Show dropdown list in cell**.
   5. Click **Save**.

   #### For the "R Year" Column:
   1. Select the cells under the "R Year" header (for example, cell F2 to F100).
   2. Click on **Data** in the menu and then choose **Data validation**.
   3. Under **Criteria**, choose **List of items** and enter: `R1, R2, R3, R4`.
   4. Click **Save**.

   _Note: Verify the actual resident years used on the Radiographics website. Adjust the drop-down items if the site uses different labels._


### 4. Populate the Spreadsheet with Article Data

1. **Arrange a Split-Screen Setup**
   - Open the Radiographics website and your Google Sheets spreadsheet side by side for easy data transfer. You can resize your browser windows or use your operating system’s split-screen feature.
   - (Tip: If you need visual instructions for split-screen setup, refer to your operating system’s documentation or search for "How to use split screen on [your OS]".)

2. **Enter Data for Each Article**
   For each article on the selected category page:

   - **Title**: Highlight the article's title on the Radiographics page, copy, and then paste into the "Title" column using Paste Special (unformatted).

   - **Author List**: Copy the list of authors. To remove any unwanted formatting, use the Paste Special command (`Ctrl+Shift+V` or `Command+Shift+V`) when pasting into the "Author List" column.

   - **Abstract**: Copy the article's abstract. If there are extra line breaks or spaces:
     - Use Paste Special to paste as unformatted text, or
     - Paste into a plain text editor (like Notepad), then copy from there and paste into Google Sheets.

   - **DOI**: Copy the DOI link from the article page and paste it into the "DOI" column.

   - **Year**: Manually type the publication year (e.g., `2019`) into the "Year" column.

   - **R Year**: From the drop-down menu in the "R Year" column, select the appropriate resident year (e.g., `R1`).

   - **Level**: From the drop-down in the "Level" column, choose the appropriate level (e.g., `Basic`).

   - **(Optional) Category**: If you are combining multiple categories in one sheet, add the category (e.g., "Breast Imaging") to the additional Category column.

3. **Repeat the Process**
   - Continue these steps for each article in the current category.
   - If working with multiple categories, either switch to another tab/sheet dedicated for that category or continue entering data in your consolidated sheet with the appropriate category noted.


### 5. Finishing Touches

1. **Enhance the Spreadsheet Layout**
   - Bold the header row for clarity.
   - Adjust column widths so that all content is readable.
   - Use cell formatting (e.g., colors for drop-down selections) as desired for better visual organization.
   - Remove any extra rows that are not used to maintain a clean, professional look.

2. **Final Review and Notification**
   - Once all data is entered and the spreadsheet is formatted to your liking, review for any inconsistencies or unwanted spaces.
   - Save your work in Google Sheets.
   - Notify stakeholders (or yourself) that the Excel/Google Sheets file is complete and ready for further processing (e.g., importing into a Python project).

---

## Final Notes

- **Text Cleaning**: The method recommended in this guide for cleaning copied text is to use "Paste Special" (i.e., pasting without formatting) or an intermediary plain text editor, which reliably removes extra formatting and unwanted characters.

- **Data Validation Setup**: Detailed GUI instructions have been provided above for creating drop-down lists on both the "Level" and "R Year" columns. If needed, refer to [Google's Data Validation Help](https://support.google.com/docs/answer/139706) for more details.

- **Multiple Categories**: Decide early whether to create separate sheets/tabs or to consolidate all data into one sheet with a category column. This decision may depend on how you plan to process the data later.

- **Resident Year Labels**: Double-check that the resident year labels on your version of the Radiographics website match the drop-down options (R1, R2, R3, R4). Adjust the drop-down list if the labels differ.

Following these instructions step-by-step will help you build a clean and organized Google Sheets chart of Radiographics Top 10 Articles, suitable for further data analysis or processing.

Happy charting!