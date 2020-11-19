import sys
import json
from data_classes.user import Main_User, Profile
import pandas as pd
from typing import List

#helps funcs
def count_elements(array: List[str]):
    data = {}
    for element in array:
        if element in data:
            data[element] += 1
        else:
            data[element] = 1
    return data

#data parsing functions
def account_dir():
    with open('./netflix-data/Account/AccountDetails.txt', 'r') as outfile:
        data = json.load(outfile)
    first_name = data['firstName']
    last_name = data['lastName']
    email_address = data['emailAddress']
    phone_number = data['phoneNumber']
    country = data['countryOfRegistration']
    membership_status = data['membershipStatus']
    account_created = data['customerCreationTimeStamp']
    return Main_User(first_name, last_name, email_address, phone_number, country, membership_status, account_created)

def profiles_dir():
    profiles_names = []
    with open('./netflix-data/Profiles/Profiles.txt') as outfile:
        for line in outfile:
            data = json.loads(line)
            profiles_names.append(data['profileName'])
    profiles = {}
    for profile in profiles_names:
        profiles.update({profile: Profile(profile)})
    return profiles

def clickstream_dir(profiles):
    csv = pd.read_csv('./netflix-data/Clickstream/Clickstream.csv')
    for i, _ in csv.iterrows():
        profile_name = csv['Profile Name'][i]
        source = csv['Source'][i]
        navigation_level = csv['Navigation Level'][i]
        if source in profiles[profile_name].cs_actions:
            if navigation_level in profiles[profile_name].cs_actions[source]:
                count = profiles[profile_name].cs_actions[source][navigation_level]
                profiles[profile_name].cs_actions[source].update({navigation_level: count+1})
            else:
                profiles[profile_name].cs_actions[source].update({navigation_level: 1})
        else:
            profiles[profile_name].cs_actions.update({source: {}})
            profiles[profile_name].cs_actions[source].update({navigation_level: 1})
    return profiles

#init funcs
def main():
    main_user = account_dir()
    profiles = profiles_dir()
    profiles = clickstream_dir(profiles)

    #result
    print(main_user.__dict__)
    for profile in profiles.values():
        print(profile.__dict__)

if __name__ == '__main__':
    main()