# How to Create a Google Spreadsheet for Radiographics Top 10 Articles

This guide provides a step-by-step process to automatically chart articles from Radiographics’ Top 10 Reading List into a structured Google Spreadsheet. You will learn how to navigate the Radiographics website, sign into Google Drive, create and format a new spreadsheet, and import data for later processing in Python.

---

# # Overview

In this task, you'll:

1. Access and navigate the Radiographics website to find the Top 10 articles.
2. Sign into your Google Drive and create a new folder and spreadsheet.
3. Configure the Google Sheet with specific column headers and set up dropdown menus using data validation.
4. Extract and format article data from the website for later use in your Python projects.
5. Finalize the spreadsheet by tidying up rows and columns.

---

# # Step-by-Step Instructions

## # 1. Access the Radiographics Top 10 Articles Page

1. Open your web browser and type **“Radiographics top 10 articles”** in the search bar.
2. From the search results, click the link titled **“RG TEAM Top 10 Reading List”** to open the Radiographics website.
3. You should see a page listing multiple categories (e.g., Breast Imaging, Cardiac, Emergency, etc.).

```

```

![To show the search results with the highlighted "RG TEAM Top 10 Reading List" link. - A screenshot of the browser search results and the Radiographics homepage displaying various article categories. - Assists users in confirming that they have accessed the correct page.](screenshots/screenshot_radiographics_homepage_1741085487.png)

## # 2. Navigate the Radiographics Website

1. Zoom in on the page if necessary to clearly view the article categories.
2. Click on any category (for example, **Breast Imaging**) to view articles organized by Resident Year (R1, R2, R3, R4, Fellows) and by difficulty level (Basic, Intermediate, Advanced).

```

```

![To display the layout with article categories segmented by resident year and level. - Screenshot of the Radiographics category page (e.g., Breast Imaging) showing sections for different residency years and article levels. - Helps users understand the website layout and where to click for further details.](screenshots/screenshot_category_view_1741085499.png)

## # 3. Log Into Google Drive

1. Open a new tab or window and navigate to **drive.google.com**.
2. If you are already signed in, verify that you are using the correct account. If not, sign out or use an incognito mode to log in.
3. Enter your email address (use a placeholder such as **your-email@example.com**) and follow the sign-in prompts. Depending on your device, you may be prompted to use a passkey or enter your password.

```

```

![To show the Google sign-in interface. - Screenshot of the Google sign-in page prompting for an email address and authentication details. - Guides users through the sign-in process required for accessing Google Drive.](screenshots/screenshot_google_login_1741085510.png)

## # 4. Create a New Folder and Spreadsheet

1. In Google Drive, click on the **New** button and then select **Folder**.
2. Name the folder **"RG-Top10-Articles"** and open it.
3. Inside this folder, click **New** again and choose **Google Sheets** to create a blank spreadsheet.
4. Rename the spreadsheet to **"Top 10 articles"**.

```

```

![To illustrate the creation of a new folder and spreadsheet in Google Drive. - Screenshot of Google Drive showing the new folder "RG-Top10-Articles" and the open Google Sheet titled "Top 10 articles". - Provides visual confirmation of the correct folder and file setup in Google Drive.](screenshots/screenshot_folder_creation_1741085521.png)

## # 5. Configure the Spreadsheet Columns and Dropdown Menus

1. In the Google Sheet, set up the following column headers using the column letters as guidance:
- **A: Abstract**
- **B: Author List**
- **C: DOI** (Digital Object Identifier)
- **D: Year**
- **E: R Year** (Resident Year)
- **F: Level**

2. To create dropdown menus for the **Level** and **R Year** columns, follow these steps:
- Select the cell range in the **Level** column where you want the dropdown (e.g., F2:F100).
- Click on **Data** in the top menu, then choose **Data validation**.
- In the Data validation window, under **Criteria**, select **List of items** and enter the options: `Basic, Intermediate, Advanced`.
- (Optional) Set background colors for each option after inserting the dropdown via manual cell formatting if desired.

- Repeat the process for the **R Year** column (e.g., E2:E100):
- Go to **Data > Data validation**.
- Under **Criteria**, select **List of items** and enter: `R1, R2, R3, R4`.
- Apply distinct colors via cell formatting if needed.

```

```

![To show the Data Validation dialog box in Google Sheets for setting up dropdown menus. - Screenshot of the Data Validation settings panel with criteria options for both the Level and R Year columns. - Helps users understand how to configure dropdown menus and see the exact options they need to input.](screenshots/screenshot_data_validation_1741085649.png)

## # 6. Importing Data from the Radiographics Website

1. Arrange your browser window so that the Radiographics website and the Google Sheet are visible side by side (split-screen view).
2. For each article in the chosen category (e.g., R1 Basic), do the following:
- **Abstract:** Copy the article abstract. To remove any unwanted formatting characters, first paste the text into your browser's address bar, then copy it again from there and paste into the **Abstract** cell in the sheet.

*Explanation: Pasting into the address bar clears any hidden formatting or extra characters that might otherwise be copied directly from the webpage.*
- **Author List:** Copy the author list text using the same technique (paste into the address bar first, then copy back) and paste it into the **Author List** cell.
- **DOI:** Copy the DOI link provided on the article page and paste it into the **DOI** column.
- **Year:** Enter the publication year (e.g., 2019) into the **Year** cell.
- **R Year:** Use the dropdown menu (populated via data validation) to select the appropriate resident year (e.g., R1).
- **Level:** Use the dropdown menu to select the correct level (e.g., Basic).

```

```

![To illustrate the split-screen view with the Radiographics website alongside the Google Sheet, and to show data being pasted into cells. - Screenshot displaying both windows with an article being processed and the respective data input fields filled in the spreadsheet. - Demonstrates how to transfer data accurately from the Radiographics page to the Google Sheet.](screenshots/screenshot_data_import_1741085548.png)

3. Repeat this process for each article across all relevant categories and resident years.

## # 7. Finalizing the Spreadsheet

1. Once all data has been imported, review the spreadsheet to ensure cells are correctly filled and formatted.
2. Remove any unnecessary rows or columns:
- To delete extra rows, right-click on the row number and select **Delete**.
- Repeat similarly for any unneeded columns.
3. Optionally, apply bold formatting to the header row (for example, select row 1 and click the **Bold** icon or press Ctrl+B) to improve visibility.
4. Ensure that the dropdown menus and color codings in the **Level** and **R Year** columns are working as intended.

*Note: While a screenshot of the final spreadsheet is not directly available from the video, carefully following the steps above will result in a neat and well-organized Google Sheet.
*

---

# # Conclusion

This guide has provided detailed, step-by-step instructions for setting up a Google Spreadsheet to chart articles from the Radiographics Top 10 Reading List. By following these steps, you will have a fully formatted spreadsheet with dropdown menus, data validation, and cleanly imported data ready for further processing in your Python projects.

Happy organizing!
