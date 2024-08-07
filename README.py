class KevinKissi(self):
        self.username = 'kevin-kissi'
        self.name = 'Kevin Kissi'
        self.web = 'https://kevinkissi.com'
        self.twitter = '@kevinkissi'
        self.linkedin = 'https://www.linkedin.com/in/kissi'
        self.source = {
            'born': ['Accra, Ghana'],
            'I have lived': ['Accra', 'Atlanta','San Francisco', 'Minneapolis', 'Fargo'],
            'Where I live': ['San Francisco, Ca'],
        }
        self.code = {
            'frontend': ['HTML', 'CSS', 'JavaScript', 'Boostrap','Node.Js','React'],
            'backend': ['Python','C#', 'PHP', 'Java', 'Django'],
            'database': ['PostgreSQL', 'MySQL', 'Casandra', 'Mongo DB'],
            'devops': ['Docker', 'Terraforms', 'AWS', 'Azure', 'Heroku'],
            'tools': ['You name it'],
            'misc': ['Firebase', 'SCRUM', 'GNU/Linux']
        }
        self.architecture = ['MVC', 'Microservices']

        def __str__(self):
            return self.name


if __name__ == '__main__':
    me = KevinKissi()

