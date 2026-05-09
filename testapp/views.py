from django.shortcuts import render
from testapp.models import Enquiry
from testapp.forms import EnquiryForm 
def home_page(request):
    return render(request,'testapp/home.html')

def students_page(request):
    return render(request,'testapp/students.html')

def faculty_page(request):
    return render(request,'testapp/faculty.html')

def events_page(request):
    return render(request,'testapp/events.html')

def enquiry_view(request):
    form = EnquiryForm()

    if request.method == 'POST':
        form = EnquiryForm(request.POST)

        if form.is_valid():
            form.save()
            form = EnquiryForm()

    return render(request, 'testapp/enquiry.html', {'form': form})

def anu_page(request):

    anu = {
        'name': 'Dr. Anu Taneja',
        'designation': 'Associate Professor',
        'subject': 'Information Technology',
        'department': 'CSE',
        'qualification': 'MTech (CSE), MCA, Ph.D',
        'email': 'anubciit@gmail.com',
        'phone': '011-49020144, 49020100',
        'address': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'specialization': 'Soft Computing, Computer Graphics',
        'interest': 'Artificial Intelligence, Optimization Algorithms, Operating System, Databases, Software Testing',
        'experience': '10+ Years',
        'image': 'images/anumam.jpg'
    }
    return render(request, 'testapp/anu.html', {'anu': anu})

def sandeep_page(request):
    sandeep = {
        'name': 'Mr. Sandeep Jain',
        'designation': 'Asstt. Professor',
        'subject': 'Computer Science',
        'department': 'CSE',
        'qualification': 'MCA, Ph.D (Pursuing)',
        'email': 'sandeepkumarbansal@gmail.com',
        'phone': '011-49020144, 49020100',
        'address': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'correspondence': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'specialization': 'DBMS, SE',
        'interest': 'OOPS, Data Structure, Software Engineering, DBMS',
        'experience': '7+ yrs'
    }

    return render(request, 'testapp/sandeep.html', {'sandeep': sandeep})

def sonia_page(request):
    sonia = {
        'name': 'Ms. Sonia Batra',
        'designation': 'Asstt. Professor',
        'subject': 'Information Technology',
        'department': 'CSE',
        'qualification': 'Ph.D. (P), MTech (CSE), MCA, BSc (Computer Applications)',
        'email': 'sonia@bciit.ac.in',
        'phone': '011-49020144, 49020100',
        'address': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'correspondence': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'specialization': 'Computer Science',
        'interest': 'Data Structures and Algorithms, Operating System, Artificial Intelligence, Software Engineering',
        'experience': '10+ Years'
    }

    return render(request, 'testapp/sonia.html', {'sonia': sonia})

def meetender_page(request):
    meetender = {
        'name': 'Mr. Meetender',
        'designation': 'Asstt. Professor',
        'subject': 'Computer Science',
        'department': 'CSE',
        'qualification': 'N/A',
        'email': 'metender@bciit.ac.in',
        'phone': '011-49020144, 49020100',
        'address': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'correspondence': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'specialization': 'Java Programming',
        'interest': 'N/A',
        'experience': '3+ years'
    }

    return render(request, 'testapp/meetender.html', {'meetender': meetender})

def shobha_page(request):
    shobha = {
        'name': 'Dr. Shobha Chawla',
        'designation': 'Associate Professor',
        'subject': 'Computer Science',
        'department': 'CSE',
        'qualification': 'M.Sc. (C.S), Ph.D. (Comp. App.), UGC (NET-JRF), SET (Rajasthan), B-Level (DOEACC)',
        'email': 'shobha@bciit.ac.in',
        'phone': 'N/A',
        'address': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'correspondence': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'specialization': 'Programming Languages, Operating System, Data Structures',
        'interest': 'Cryptography, Cloud Computing, Machine Learning',
        'experience': '11+ Years'
    }

    return render(request, 'testapp/shobha.html', {'shobha': shobha})
def alok_page(request):
    alok = {
        'name': 'Mr. Alok Mishra',
        'designation': 'Asst. Professor',
        'subject': 'Computer Science',
        'department': 'CSE',
        'qualification': 'Ph.D (Pursuing) in CSE, MTech, M.Sc (IT), MCA, NIELIT O & A Level',
        'email': 'alok@bciit.ac.in',
        'phone': 'N/A',
        'address': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'correspondence': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'specialization': 'Programming Languages C, C++, Java (Core), Python, MySQL, Django',
        'interest': 'Software Development and Artificial Intelligence',
        'experience': '14+ years'
    }

    return render(request, 'testapp/alok.html', {'alok': alok})

def sanjna_page(request):
    sanjna = {
        'name': 'Ms. Sanjana Gulia',
        'designation': 'Asst. Professor',
        'subject': 'English Literature',
        'department': 'Computer Science',
        'qualification': 'PhD (P), M.Ed (P), MA (English), B.Ed, English Honours, PGDFCS, DCE, UGC-NET',
        'email': 'sanjna@bciit.ac.in',
        'phone': '09990914697',
        'address': 'N/A',
        'correspondence': 'N/A',
        'specialization': 'English Literature',
        'interest': 'English Literature and Communication',
        'experience': '3 Years'
    }

    return render(request, 'testapp/sanjna.html', {'sanjna': sanjna})

def preeti_page(request):
    preeti = {
        'name': 'Ms. Preeti Sharma',
        'designation': 'Assistant Professor',
        'subject': 'Operating System, Cyber Law & Ethics, Data Structure, Software Engineering',
        'department': 'CSE',
        'qualification': 'M.Tech (IT), M.Sc (CS), BCA',
        'email': 'preeti@bciit.ac.in',
        'phone': 'N/A',
        'address': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'correspondence': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'specialization': 'N/A',
        'interest': 'AI & ML, Fog Computing',
        'experience': '1 year 8 months'
    }

    return render(request, 'testapp/preeti.html', {'preeti': preeti})

def pallavi_page(request):
    pallavi = {
        'name': 'Ms. Pallavi Bhatt',
        'designation': 'Assistant Professor',
        'subject': 'Computer Graphics, DBMS, Data Structures, Operating System, Software Engineering, OOAD, C, C++, Python',
        'department': 'BCA and MCA',
        'qualification': 'B.E. (ECT), M.Tech (CSE)',
        'email': 'pallavibhatt@bciit.ac.in',
        'phone': '011-49020144',
        'address': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi',
        'correspondence': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi',
        'specialization': 'Computer Graphics, DBMS, Data Structures, Operating System',
        'interest': 'Computer Science',
        'experience': '20 Years'
    }

    return render(request, 'testapp/pallavi.html', {'pallavi': pallavi})

def harsh_page(request):
    harsh = {
        'name': 'Dr. Harsh Arora',
        'designation': 'Associate Professor',
        'subject': 'Data Structures, Machine Learning',
        'department': 'CSE',
        'qualification': 'Ph.D (CSE), UGC-NET, M.Tech (CSE), MCA, MBA (HR), B.Sc',
        'email': 'harsh@bciit.ac.in',
        'phone': '011-49020144, 49020100',
        'address': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'correspondence': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'specialization': 'Data Structures, Machine Learning',
        'interest': 'Algorithms, Deep Learning, Artificial Intelligence, Machine Learning, Operating System, Software Engineering, E-Commerce, Object Oriented Programming, Python, C, C++, Database',
        'experience': '18 Years'
    }

    return render(request, 'testapp/harsh.html', {'harsh': harsh})

def kritika_page(request):
    kritika = {
        'name': 'Ms Kritika',
        'designation': 'Assistant Professor',
        'subject': 'Computer Science',
        'department': 'CSE',
        'qualification': 'MCA, B.Sc. (Comp. Sci.)',
        'email': 'kritika@bciit.ac.in',
        'phone': 'N/A',
        'address': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'correspondence': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'specialization': 'Programming Languages, Data Structure',
        'interest': 'Java, C, C++, OOPs, Computer Organisation and Architecture, Database Management Systems',
        'experience': 'N/A'
    }

    return render(request, 'testapp/kritika.html', {'kritika': kritika})
def lekhram_page(request):
    lekhram = {
        'name': 'Mr. Lekhram Prajapati',
        'designation': 'Assistant Professor',
        'subject': 'Computer Science',
        'department': 'CSE',
        'qualification': 'B.Sc, M.C.A, B.Ed, Pursuing Ph.D. (Comp. App.)',
        'email': 'lekhram@bciit.ac.in',
        'phone': 'N/A',
        'address': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'correspondence': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'specialization': 'Programming Languages, Computer Network, Data Structures, Database',
        'interest': 'Cybersecurity, Artificial Intelligence, Machine Learning',
        'experience': '13+ Years'
    }

    return render(request, 'testapp/lekhram.html', {'lekhram': lekhram})

def monika_page(request):
    monika = {
        'name': 'Ms Monika Chawla',
        'designation': 'Assistant Professor',
        'subject': 'Computer Science',
        'department': 'CSE',
        'qualification': 'A-Level (DOEACC), M.Sc. (I.T.), MCA, M.E (CSE), Ph.D. Pursuing from Manav Rachna International Institute of Research & Studies',
        'email': 'monika@bciit.ac.in',
        'phone': 'N/A',
        'address': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'correspondence': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'specialization': 'Programming Languages, Digital Electronics, Operating System, Data Structures and Software Engineering',
        'interest': 'Image Processing and Machine Learning',
        'experience': '22+ Years'
    }

    return render(request, 'testapp/monika.html', {'monika': monika})

def palak_page(request):
    palak = {
        'name': 'Palak Sharma',
        'designation': 'Assistant Professor cum Placement Officer',
        'subject': 'Professional Proficiency (Professional Ethics, Organisation Behavior, Human Values)',
        'department': 'IT',
        'qualification': 'MBA in Finance and Marketing, M.Com, B.Com, B.Ed. in Commerce and Computer, Three-year Diploma in Software Engineering',
        'email': 'palak@bciit.ac.in',
        'phone': 'N/A',
        'address': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'correspondence': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'specialization': 'Communication',
        'interest': 'Business Communication, Professional Proficiency, OB, Finance',
        'experience': '12+ Years'
    }

    return render(request, 'testapp/palak.html', {'palak': palak})

def keshav_page(request):
    keshav = {
        'name': 'Mr. Keshav Kaushik',
        'designation': 'Assistant Professor',
        'subject': 'Mathematics',
        'department': 'Computer Science',
        'qualification': 'M.Sc. (Mathematics), Ph.D. (Pursuing)',
        'email': 'keshav@bciit.ac.in',
        'phone': 'N/A',
        'address': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'correspondence': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'specialization': 'Pure Mathematics',
        'interest': 'N/A',
        'experience': '4 Years'
    }

    return render(request, 'testapp/keshav.html', {'keshav': keshav})

def smriti_page(request):
    smriti = {
        'name': 'Ms. Smriti Sharma',
        'designation': 'Assistant Professor',
        'subject': 'Computer Science and Engineering',
        'department': 'MCA',
        'qualification': 'Pursuing PhD, M.Tech (CSE), M.B.A. (HRM), B.Tech (CSE)',
        'email': 'smritisharma3627@gmail.com',
        'phone': '011-49020147',
        'address': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'correspondence': 'Chandiwala Estate, Maa Anandmai Marg, Kalkaji, Delhi-110019',
        'specialization': 'Data Science, Artificial Intelligence',
        'interest': 'Intelligent Systems, Information Retrieval, Data Science, Software Project Management',
        'experience': '10 Years'
    }

    return render(request, 'testapp/smriti.html', {'smriti': smriti})