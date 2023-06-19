import smtplib
import requests


def send_mail(movie_data, to_addrs=""):  # NOTE: add your default email here
    # NOTE: Your email and password
    my_email = ""
    password = ""
    message = "Subject:Breif Information on LOTR Movies lore\n\n"

    for data in movie_data:
        prompt = f'''
        Movie: {data['name']}
        Runtime: {data['runtimeInMinutes']} minutes
        Budget: ${data['budgetInMillions']} million
        Box Office Revenue: ${data['boxOfficeRevenueInMillions']} million
        Academy Award Nominations: {data['academyAwardNominations']}
        Academy Award Wins: {data['academyAwardWins']}
        Rotten Tomatoes Score: {data['rottenTomatoesScore']}%
        '''
        message += (prompt)

    # print(message)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
                from_addr=my_email,
                to_addrs=to_addrs,
                msg=message
                )


def get_data():
    base_url = "https://the-one-api.dev/v2"
    # NOTE: Your token
    endpoint = "/movie"
    bearer_token = ''

    headers = {
            "Authorization": "Bearer " + bearer_token,
            }

    response = requests.get(base_url + endpoint, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return (data['docs'])
    else:
        # Error occurred
        print("Error:", response.status_code)


if __name__ == "__main__":
    enter_email = input("Do you want to enter the receiver's email? (y/n): ")
    if enter_email.lower() == 'y':
        receiver_email = input("Enter the email you want to send the LOTR movies lore to: ")
    else:
        receiver_email = ""

    if receiver_email:
        data = get_data()
        send_mail(data, receiver_email)
