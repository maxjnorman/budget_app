def get_archive_date():
    return (timezone.now() + timedelta(days=14)).date
