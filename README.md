# Fifa Ultimate Team DB
Web scraping project I did using Python and Selenium to get all UT players from https://wefut.com/player-database. Probably not the most efficient way of doing this but it still works.

# Notes
The scripts create csv files to save the information, but feel free to change how the information is saved.

For practical reasons in the scripts I only include the following attributes: **Name,	Rating,	Position,	Card type,	Region,	PAC,	SHO,	PAS, DRI,	DEF,	PHY and	Link**

But if you want to add the rest of the attributes of the players you can do so by adding their XPath along with the others (using the same format).

#TODO
- Use Python Requests module to improve the efficiency of the scripts
