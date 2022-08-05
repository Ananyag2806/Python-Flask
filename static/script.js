// document.getElementById('basic').addEventListener('click', displayInfo)
document.getElementById('loanForm').addEventListener('submit', displayInfo)

function displayPrediction() {
    document.getElementById('output').style.display = 'block'
}

function displayInfo (e) {
    e.preventDefault()

    let gender = document.getElementById('gender').value
    let no_of_dependents = document.getElementById('no_of_dependents').value
    let education = document.getElementById('education').value
    let married = document.getElementById('married').value
    let self_employed = document.getElementById('self_employed').value
    let applicant_income = document.getElementById('applicant_income').value
    let coapplicant_income = document.getElementById('coapplicant_income').value
    let loan_amount = document.getElementById('loan_amount').value
    let loan_amount_term = document.getElementById('loan_amount_term').value
    let credit_history = document.getElementById('credit_history').value
    let property_area = document.getElementById('property_area').value


    fetch('http://127.0.0.1:5000/', {
        method : 'POST',
        headers : {
            'Content-Type':'application/json'
        },
        body : JSON.stringify({
            "gender" : gender,
            "no_of_dependents" : no_of_dependents,
            "education" : education,
            "self_employed" : self_employed,
            "married" : married,
            "applicant_income" : applicant_income,
            "coapplicant_income" : coapplicant_income,
            "loan_amount" : loan_amount,
            "loan_amount_term" : loan_amount_term,
            "credit_history" : credit_history,
            "property_area" : property_area
         })
    })
        .then(function (response) {
            return response.json()
        })
        .then(function (data) {
            if (data.predicted_value == 'Y') {
                Loan_Status = 'Accepted'
            }
           
            else {
                Loan_Status = 'Rejected'
            }
            document.getElementById('output').innerHTML = `Your Loan is ${Loan_Status}`
        })
}