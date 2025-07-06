# Rugby Scores Scraper & Visualizer

A Django web application that scrapes rugby match results from the BBC Sport website and creates interactive visualizations using Plotly. Built following BugBytes' tutorial, this project demonstrates web scraping with BeautifulSoup4, data storage with Django models, and data visualization with Plotly.

## Features

- **Primary Goal**: Demonstrate web scraping and Plotly visualization techniques
- **Web Scraping**: Automatically scrapes rugby match results from BBC Sport
- **Data Storage**: Stores fixture data in a SQLite database using Django ORM
- **Data Visualization**: Creates interactive bar charts showing team performance
- **Management Commands**: Custom Django management command for automated scraping
- **Responsive Web Interface**: Clean, simple web interface to view the charts

## Screenshots

![Rugby Scores Bar Chart](https://github.com/user-attachments/assets/4dbf7791-2ed3-445f-8273-df06aaeda972)

## Technologies Used

- **Backend**: Django 4.1.4
- **Web Scraping**: BeautifulSoup4, Requests
- **Data Visualization**: Plotly Express
- **Database**: SQLite
- **Python**: 3.x

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SvetozarP/DjangoBSScrapePlotly.git
   cd DjangoBSScrapePlotly
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django beautifulsoup4 requests plotly django-extensions
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## Usage

### Scraping Data

To scrape rugby results from the BBC Sport website:

```bash
python manage.py scrape_results
```

This command will:
- Scrape match results from April 29, 2025 to May 27, 2025
- Store the data in the SQLite database
- Avoid duplicate entries using `get_or_create()`

### Viewing Results

1. Start the Django development server
2. Open your browser and navigate to `http://127.0.0.1:8000/`
3. View the interactive bar chart showing total scores by team

## Project Structure

```
DjangoBSScrapePlotly/
├── core/                          # Main Django app
│   ├── management/
│   │   └── commands/
│   │       └── scrape_results.py  # Custom management command
│   ├── migrations/                # Database migrations
│   ├── templates/                 # HTML templates
│   │   ├── base.html
│   │   └── index.html
│   ├── models.py                  # Fixture model
│   ├── views.py                   # View logic and chart generation
│   └── urls.py                    # URL configuration
├── world_cup/                     # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── .gitignore
└── README.md
```

## Data Model

The application uses a simple `Fixture` model to store match data:

```python
class Fixture(models.Model):
    team1 = models.CharField(max_length=128)      # Home team
    team2 = models.CharField(max_length=128)      # Away team
    team1_goals = models.IntegerField()           # Home team score
    team2_goals = models.IntegerField()           # Away team score
```

## Customization

### Changing Date Range

To scrape different date ranges, modify the constants in `core/management/commands/scrape_results.py`:

```python
START_DATE = datetime(2025, 4, 29)  # Change start date
END_DATE = datetime(2025, 5, 27)    # Change end date
```

### Modifying Chart Appearance

Update the chart configuration in `core/views.py`:

```python
fig = px.bar(
    x=scores_sc.keys(),
    y=scores_sc.values(),
    title='Your Custom Title',
    height=800,
    # Add more Plotly customization options
)
```

## How It Works

1. **Web Scraping**: The management command constructs URLs for each day in the specified date range and scrapes match results using BeautifulSoup4
2. **Data Processing**: Match data is parsed and stored in the database, with duplicate prevention
3. **Visualization**: The view aggregates scores by team and creates an interactive bar chart using Plotly
4. **Web Interface**: The chart is rendered in a simple HTML template

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built following [BugBytes' tutorial](https://www.youtube.com/@BugBytes)
- BBC Sport for providing the rugby results data
- Django and Plotly communities for excellent documentation

## Future Enhancements

- [ ] Add support for different sports
- [ ] Implement team performance trends over time
- [ ] Add filtering and sorting options
- [ ] Include match dates in the database
- [ ] Add team logos and additional metadata
- [ ] Implement automated daily scraping with cron jobs
