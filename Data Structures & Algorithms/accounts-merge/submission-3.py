class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # accounts[i] is a list of strings where:
            # the first elm is a name
            # the rest are emaisl linked to the account
        # Merge these accounts
            # Two accounts belong to the same person if there is a common email to both accounts
            # Just because two accounts have the same name, doesn't mean they belong to the same person
        # After meging the accounts, return the accounts in the following format: 
            # the first element of each account is the name, and the rest of the elements are emails in sorted order
        
    










        # We could maintain two dictionaries
            # One that maps emails to a user: called users
            # One that maps a user to emails: called emails
        
        # We use users to see if an email has been associated with a user (user in this case will be the idx instead of name)
        users = defaultdict(set)
        # We use emails to see if what emails are associated with a user (user in this case will be the idx instead of name)
        emails = defaultdict(set)

        # go through accounts and map users to their emails and vice versa
        for idx, account in enumerate(accounts):

            # check to see if any of the emails 
            # are alr associated with a user
            
            # find the accts to merge
            to_merge = set()
            merged_emails = set()
            for ei in range(1, len(account)):
                email = account[ei]
                if email in users:
                    # there is a user associated with this email
                    # so save that user 
                    to_merge.add(users[email])
                # include this email in the merged account
                merged_emails.add(email)
            
            # go through the other accounts and include their emails into the newly merged account
            for user in to_merge:
                for email in emails[user]:
                    # create the consolidated email list
                    merged_emails.add(email)
                    # overwrite the email to point to the newly merged account
                    users[email] = idx                
                del emails[user]
            
            # save the newly merged account
            emails[idx] = merged_emails
            for email in merged_emails:
                users[email] = idx


        res = []
        for acctIdx, emails in emails.items():
            name = accounts[acctIdx][0]
            emails = list(emails)
            emails.sort()

            mergedAcct = [name]
            mergedAcct.extend(emails)
            res.append(mergedAcct)

        return res




























