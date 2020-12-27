from flask import Flask, jsonify,request
#from sklearn.externals import joblib
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def home():
    return 'Fraud_app !!'

@app.route('/predict', methods=['POST'])
def predict():
    
    if request.method == "POST":
        json_ = request.get_json(silent=True)
        print(json_)
            
        months_as_customer=json_.get('months_as_customer')
        age=json_.get('age')
        policy_csl=json_.get('policy_csl')
        policy_deductable=json_.get('policy_deductable')
        policy_annual_premium=json_.get('policy_annual_premium')
        umbrella_limit=json_.get('umbrella_limit')
        capital_gains=json_.get('capital-gains')
        capital_loss=json_.get('capital-loss')
        incident_hour_of_the_day=json_.get('incident_hour_of_the_day')
        number_of_vehicles_involved=json_.get('number_of_vehicles_involved')
        bodily_injuries=json_.get('bodily_injuries')
        witnesses=json_.get('witnesses')
        total_claim_amount=json_.get('total_claim_amount')
        injury_claim=json_.get('injury_claim')
        property_claim=json_.get('property_claim')
        vehicle_claim=json_.get('vehicle_claim')
        auto_year=json_.get('auto_year')
        
        
        # insured_occupation
            # adm-clerical = 0 (not in column)
        insured_occupation=json_.get('insured_occupation')
        if(insured_occupation=='machine-op-inspct'):
            
            insured_occupation_armed_forces=0
            insured_occupation_craft_repair=0
            insured_occupation_exec_managerial=0
            insured_occupation_farming_fishing=0
            insured_occupation_handlers_cleaners=0
            insured_occupation_machine_op_inspct=1
            insured_occupation_other_service=0
            insured_occupation_priv_house_serv=0
            insured_occupation_prof_specialty=0
            insured_occupation_protective_serv=0
            insured_occupation_sales=0
            insured_occupation_tech_support=0
            insured_occupation_transport_moving=0
    
        elif (insured_occupation=='prof-specialty'):
            insured_occupation_armed_forces=0
            insured_occupation_craft_repair=0
            insured_occupation_exec_managerial=0
            insured_occupation_farming_fishing=0
            insured_occupation_handlers_cleaners=0
            insured_occupation_machine_op_inspct=0
            insured_occupation_other_service=0
            insured_occupation_priv_house_serv=0
            insured_occupation_prof_specialty=1
            insured_occupation_protective_serv=0
            insured_occupation_sales=0
            insured_occupation_tech_support=0
            insured_occupation_transport_moving=0
    
        elif (insured_occupation=='tech-support'):
            insured_occupation_armed_forces=0
            insured_occupation_craft_repair=0
            insured_occupation_exec_managerial=0
            insured_occupation_farming_fishing=0
            insured_occupation_handlers_cleaners=0
            insured_occupation_machine_op_inspct=0
            insured_occupation_other_service=0
            insured_occupation_priv_house_serv=0
            insured_occupation_prof_specialty=0
            insured_occupation_protective_serv=0
            insured_occupation_sales=0
            insured_occupation_tech_support=1
            insured_occupation_transport_moving=0
                
        elif (insured_occupation=='exec-managerial'):
            insured_occupation_armed_forces=0
            insured_occupation_craft_repair=0
            insured_occupation_exec_managerial=1
            insured_occupation_farming_fishing=0
            insured_occupation_handlers_cleaners=0
            insured_occupation_machine_op_inspct=0
            insured_occupation_other_service=0
            insured_occupation_priv_house_serv=0
            insured_occupation_prof_specialty=0
            insured_occupation_protective_serv=0
            insured_occupation_sales=0
            insured_occupation_tech_support=0
            insured_occupation_transport_moving=0
                
        elif (insured_occupation=='sales'):
            insured_occupation_armed_forces=0
            insured_occupation_craft_repair=0
            insured_occupation_exec_managerial=0
            insured_occupation_farming_fishing=0
            insured_occupation_handlers_cleaners=0
            insured_occupation_machine_op_inspct=0
            insured_occupation_other_service=0
            insured_occupation_priv_house_serv=0
            insured_occupation_prof_specialty=0
            insured_occupation_protective_serv=0
            insured_occupation_sales=1
            insured_occupation_tech_support=0
            insured_occupation_transport_moving=0
                
        elif (insured_occupation=='craft-repair'):
            insured_occupation_armed_forces=0
            insured_occupation_craft_repair=1
            insured_occupation_exec_managerial=0
            insured_occupation_farming_fishing=0
            insured_occupation_handlers_cleaners=0
            insured_occupation_machine_op_inspct=0
            insured_occupation_other_service=0
            insured_occupation_priv_house_serv=0
            insured_occupation_prof_specialty=0
            insured_occupation_protective_serv=0
            insured_occupation_sales=0
            insured_occupation_tech_support=0
            insured_occupation_transport_moving=0
    
        elif (insured_occupation=='transport-moving'):
            insured_occupation_armed_forces=0
            insured_occupation_craft_repair=0
            insured_occupation_exec_managerial=0
            insured_occupation_farming_fishing=0
            insured_occupation_handlers_cleaners=0
            insured_occupation_machine_op_inspct=0
            insured_occupation_other_service=0
            insured_occupation_priv_house_serv=0
            insured_occupation_prof_specialty=0
            insured_occupation_protective_serv=0
            insured_occupation_sales=0
            insured_occupation_tech_support=0
            insured_occupation_transport_moving=1
                
        elif (insured_occupation=='priv-house-serv'):
            insured_occupation_armed_forces=0
            insured_occupation_craft_repair=0
            insured_occupation_exec_managerial=0
            insured_occupation_farming_fishing=0
            insured_occupation_handlers_cleaners=0
            insured_occupation_machine_op_inspct=0
            insured_occupation_other_service=0
            insured_occupation_priv_house_serv=1
            insured_occupation_prof_specialty=0
            insured_occupation_protective_serv=0
            insured_occupation_sales=0
            insured_occupation_tech_support=0
            insured_occupation_transport_moving=0
    
        elif (insured_occupation=='other-service'):
            insured_occupation_armed_forces=0
            insured_occupation_craft_repair=0
            insured_occupation_exec_managerial=0
            insured_occupation_farming_fishing=0
            insured_occupation_handlers_cleaners=0
            insured_occupation_machine_op_inspct=0
            insured_occupation_other_service=1
            insured_occupation_priv_house_serv=0
            insured_occupation_prof_specialty=0
            insured_occupation_protective_serv=0
            insured_occupation_sales=0
            insured_occupation_tech_support=0
            insured_occupation_transport_moving=0
    
        elif (insured_occupation=='armed-forces'):
            insured_occupation_armed_forces=1
            insured_occupation_craft_repair=0
            insured_occupation_exec_managerial=0
            insured_occupation_farming_fishing=0
            insured_occupation_handlers_cleaners=0
            insured_occupation_machine_op_inspct=0
            insured_occupation_other_service=0
            insured_occupation_priv_house_serv=0
            insured_occupation_prof_specialty=0
            insured_occupation_protective_serv=0
            insured_occupation_sales=0
            insured_occupation_tech_support=0
            insured_occupation_transport_moving=0
                
                
                
        elif (insured_occupation=='protective-serv'):
            insured_occupation_armed_forces=0
            insured_occupation_craft_repair=0
            insured_occupation_exec_managerial=0
            insured_occupation_farming_fishing=0
            insured_occupation_handlers_cleaners=0
            insured_occupation_machine_op_inspct=0
            insured_occupation_other_service=0
            insured_occupation_priv_house_serv=0
            insured_occupation_prof_specialty=0
            insured_occupation_protective_serv=1
            insured_occupation_sales=0
            insured_occupation_tech_support=0
            insured_occupation_transport_moving=0
                
        elif (insured_occupation=='handlers-cleaners'):
            insured_occupation_armed_forces=0
            insured_occupation_craft_repair=0
            insured_occupation_exec_managerial=0
            insured_occupation_farming_fishing=0
            insured_occupation_handlers_cleaners=1
            insured_occupation_machine_op_inspct=0
            insured_occupation_other_service=0
            insured_occupation_priv_house_serv=0
            insured_occupation_prof_specialty=0
            insured_occupation_protective_serv=0
            insured_occupation_sales=0
            insured_occupation_tech_support=0
            insured_occupation_transport_moving=0
                
        elif (insured_occupation=='farming-fishing'):
            insured_occupation_armed_forces=0
            insured_occupation_craft_repair=0
            insured_occupation_exec_managerial=0
            insured_occupation_farming_fishing=1
            insured_occupation_handlers_cleaners=0
            insured_occupation_machine_op_inspct=0
            insured_occupation_other_service=0
            insured_occupation_priv_house_serv=0
            insured_occupation_prof_specialty=0
            insured_occupation_protective_serv=0
            insured_occupation_sales=0
            insured_occupation_tech_support=0
            insured_occupation_transport_moving=0
             
    
        else:
            insured_occupation_armed_forces=0
            insured_occupation_craft_repair=0
            insured_occupation_exec_managerial=0
            insured_occupation_farming_fishing=0
            insured_occupation_handlers_cleaners=0
            insured_occupation_machine_op_inspct=0
            insured_occupation_other_service=0
            insured_occupation_priv_house_serv=0
            insured_occupation_prof_specialty=0
            insured_occupation_protective_serv=0
            insured_occupation_sales=0
            insured_occupation_tech_support=0
            insured_occupation_transport_moving=0
        
        
        
        # insured_relationship
            # husband = 0 (not in column)
        insured_relationship=json_.get('insured_relationship')
        if(insured_relationship=='own-child'):
            insured_relationship_not_in_family=0
            insured_relationship_other_relative=0
            insured_relationship_own_child=1
            insured_relationship_unmarried=0
            insured_relationship_wife=0
                
        elif(insured_relationship=='other-relative'):
            insured_relationship_not_in_family=0
            insured_relationship_other_relative=1
            insured_relationship_own_child=0
            insured_relationship_unmarried=0
            insured_relationship_wife=0
                
        elif(insured_relationship=='not-in-family'):
            insured_relationship_not_in_family=1
            insured_relationship_other_relative=0
            insured_relationship_own_child=0
            insured_relationship_unmarried=0
            insured_relationship_wife=0
                
        elif(insured_relationship=='wife'):
            insured_relationship_not_in_family=0
            insured_relationship_other_relative=0
            insured_relationship_own_child=0
            insured_relationship_unmarried=0
            insured_relationship_wife=1
                
        elif(insured_relationship=='unmarried'):
            insured_relationship_not_in_family=0
            insured_relationship_other_relative=0
            insured_relationship_own_child=0
            insured_relationship_unmarried=1
            insured_relationship_wife=0
                
                
        else:
            insured_relationship_not_in_family=0
            insured_relationship_other_relative=0
            insured_relationship_own_child=0
            insured_relationship_unmarried=0
            insured_relationship_wife=0
                
                
                
        # policy_state
            # IL = 0 (not in column)
        policy_state=json_.get('policy_state')
            
        if(policy_state=='OH'):
            policy_state_IN=0
            policy_state_OH=1
            
        elif(policy_state=='IN'):
            policy_state_IN=1
            policy_state_OH=0
                
        else:
            policy_state_IN=0
            policy_state_OH=0
                
        # insured_sex
            # IL = 0 (not in column)
        insured_sex=json_.get('insured_sex')
            
        if (insured_sex=='MALE'):
            insured_sex=0
        else:
            insured_sex=1
                
        # collision_type
            # Front Collision = 0 (not in column)
        collision_type=json_.get('collision_type')
            
        if(collision_type=='Rear Collision'):
            collision_type_Rear_Collision=1
            collision_type_Side_Collision=0
            collision_type_Unknown=0
                
        elif(collision_type=='Side Collision'):
            collision_type_Rear_Collision=0
            collision_type_Side_Collision=1
            collision_type_Unknown=0
                
        elif(collision_type=='Unknown'):
            collision_type_Rear_Collision=0
            collision_type_Side_Collision=0
            collision_type_Unknown=1
                
        else:
            collision_type_Rear_Collision=0
            collision_type_Side_Collision=0
            collision_type_Unknown=0
                
            
        # incident_severity
            # Major Damage = 0 (not in column)
        incident_severity=json_.get('incident_severity')
            
        if(incident_severity=='Minor Damage'):
            incident_severity_Minor_Damage=1
            incident_severity_Total_Loss=0
            incident_severity_Trivial_Damage=0
                
        elif(incident_severity=='Total Loss'):
            incident_severity_Minor_Damage=0
            incident_severity_Total_Loss=1
            incident_severity_Trivial_Damage=0
                
        elif(incident_severity=='Trivial Damage'):
            incident_severity_Minor_Damage=0
            incident_severity_Total_Loss=0
            incident_severity_Trivial_Damage=1
                
        else:
            incident_severity_Minor_Damage=0
            incident_severity_Total_Loss=0
            incident_severity_Trivial_Damage=0
            
        # authorities_contacted
            # Ambulance = 0 (not in column)
        authorities_contacted=json_.get('authorities_contacted')
            
        if(authorities_contacted=='Police'):
            authorities_contacted_Fire=0
            authorities_contacted_None=0
            authorities_contacted_Other=0
            authorities_contacted_Police=1
                
        elif(authorities_contacted=='Fire'):
            authorities_contacted_Fire=1
            authorities_contacted_None=0
            authorities_contacted_Other=0
            authorities_contacted_Police=0
            
        elif(authorities_contacted=='Other'):
            authorities_contacted_Fire=0
            authorities_contacted_None=0
            authorities_contacted_Other=1
            authorities_contacted_Police=0
                
        elif(authorities_contacted=='None'):
            authorities_contacted_Fire=0
            authorities_contacted_None=1
            authorities_contacted_Other=0
            authorities_contacted_Police=0
                
        else:
            authorities_contacted_Fire=0
            authorities_contacted_None=0
            authorities_contacted_Other=0
            authorities_contacted_Police=0
            
         # incident_state
            # NC = 0 (not in column)
        incident_state=json_.get('incident_state')
            
        if(incident_state=='NY'):
            incident_state_NY=1
            incident_state_OH=0
            incident_state_PA=0
            incident_state_SC=0
            incident_state_VA=0
            incident_state_WV=0
                
        elif(incident_state=='SC'):
            incident_state_NY=0
            incident_state_OH=0
            incident_state_PA=0
            incident_state_SC=1
            incident_state_VA=0
            incident_state_WV=0
                
        elif(incident_state=='WV'):
            incident_state_NY=0
            incident_state_OH=0
            incident_state_PA=0
            incident_state_SC=0
            incident_state_VA=0
            incident_state_WV=1
                
        elif(incident_state=='VA'):
            incident_state_NY=0
            incident_state_OH=0
            incident_state_PA=0
            incident_state_SC=0
            incident_state_VA=1
            incident_state_WV=0
                
        elif(incident_state=='PA'):
            incident_state_NY=0
            incident_state_OH=0
            incident_state_PA=1
            incident_state_SC=0
            incident_state_VA=0
            incident_state_WV=0
                
        else:
            incident_state_NY=0
            incident_state_OH=0
            incident_state_PA=0
            incident_state_SC=0
            incident_state_VA=0
            incident_state_WV=0
                
                
                
        # incident_city
            # Arlington = 0 (not in column)
        incident_city=json_.get('incident_city')
            
        if(incident_city=='Springfield'):
            incident_city_Columbus=0
            incident_city_Hillsdale=0
            incident_city_Northbend=0
            incident_city_Northbrook=0
            incident_city_Riverwood=0
            incident_city_Springfield=1
                
        elif(incident_city=='Columbus'):
            incident_city_Columbus=1
            incident_city_Hillsdale=0
            incident_city_Northbend=0
            incident_city_Northbrook=0
            incident_city_Riverwood=0
            incident_city_Springfield=0
            
        elif(incident_city=='Northbend'):
            incident_city_Columbus=0
            incident_city_Hillsdale=0
            incident_city_Northbend=1
            incident_city_Northbrook=0
            incident_city_Riverwood=0
            incident_city_Springfield=0
                
        elif(incident_city=='Hillsdale'):
            incident_city_Columbus=0
            incident_city_Hillsdale=1
            incident_city_Northbend=0
            incident_city_Northbrook=0
            incident_city_Riverwood=0
            incident_city_Springfield=0
                
        elif(incident_city=='Riverwood'):
            incident_city_Columbus=0
            incident_city_Hillsdale=0
            incident_city_Northbend=0
            incident_city_Northbrook=0
            incident_city_Riverwood=1
            incident_city_Springfield=0
                    
        elif(incident_city=='Northbrook'):
            incident_city_Columbus=0
            incident_city_Hillsdale=0
            incident_city_Northbend=0
            incident_city_Northbrook=1
            incident_city_Riverwood=0
            incident_city_Springfield=0
                
        else:
            incident_city_Columbus=0
            incident_city_Hillsdale=0
            incident_city_Northbend=0
            incident_city_Northbrook=0
            incident_city_Riverwood=0
            incident_city_Springfield=0
                
                
                
        # property_damage
            # NO = 0 (not in column)
        property_damage=json_.get('property_damage')
            
        if(property_damage=='Unknown'):
            property_damage_Unknown=1
            property_damage_YES=0
                
        elif(property_damage=='YES'):
            property_damage_Unknown=0
            property_damage_YES=1
                
        else:
            property_damage_Unknown=0
            property_damage_YES=0
                
        # insured_education_level
            # MD = 0 (not in column)
        insured_education_level=json_.get('insured_education_level')
            
        if(insured_education_level=='High School'):
            insured_education_level=0
                
        elif(insured_education_level=='JD'):
            insured_education_level=1
                
        elif(insured_education_level=='College'):
            insured_education_level=2
                
        elif(insured_education_level=='Masters'):
            insured_education_level=3
                
        elif(insured_education_level=='Associate'):
            insured_education_level=4
                
        elif(insured_education_level=='PhD'):
            insured_education_level=5
                
        else:
            insured_education_level=6
                
         # incident_type
            # Multi-vehicle Collision = 0 (not in column)
        incident_type=json_.get('incident_type')
            
        if(incident_type=='Single Vehicle Collision'):
            incident_type_Parked_Car=0
            incident_type_Single_Vehicle_Collision=1
            incident_type_Vehicle_Theft=0
                
        elif(incident_type=='SVehicle Theft'):
            incident_type_Parked_Car=0
            incident_type_Single_Vehicle_Collision=0
            incident_type_Vehicle_Theft=1
                
        elif(incident_type=='Parked Car'):
            incident_type_Parked_Car=1
            incident_type_Single_Vehicle_Collision=0
            incident_type_Vehicle_Theft=0
                
        else:
            incident_type_Parked_Car=0
            incident_type_Single_Vehicle_Collision=0
            incident_type_Vehicle_Theft=0
                
        # police_report_available
            # NO = 0 (not in column)
        police_report_available=json_.get('police_report_available')
            
        if(police_report_available=='Unknown'):
            police_report_available_Unknown=1
            police_report_available_YES=0
                
        elif(police_report_available=='YES'):
            police_report_available_Unknown=0
            police_report_available_YES=1
                
        else:
            police_report_available_Unknown=0
            police_report_available_YES=0
                
        
        
        prediction = clf.predict([[months_as_customer,
        age,
        policy_csl,
        policy_deductable,
        policy_annual_premium,
        umbrella_limit,
        insured_sex,
        insured_education_level,
        capital_gains,
        capital_loss,
        incident_hour_of_the_day,
        number_of_vehicles_involved,
        bodily_injuries,
        witnesses,
        total_claim_amount,
        injury_claim,
        property_claim,
        vehicle_claim,
        auto_year,
        policy_state_IN,
        policy_state_OH,
        insured_occupation_armed_forces,
        insured_occupation_craft_repair,
        insured_occupation_exec_managerial,
        insured_occupation_farming_fishing,
        insured_occupation_handlers_cleaners,
        insured_occupation_machine_op_inspct,
        insured_occupation_other_service,
        insured_occupation_priv_house_serv,
        insured_occupation_prof_specialty,
        insured_occupation_protective_serv,
        insured_occupation_sales,
        insured_occupation_tech_support,
        insured_occupation_transport_moving,
        insured_relationship_not_in_family,
        insured_relationship_other_relative,
        insured_relationship_own_child,
        insured_relationship_unmarried,
        insured_relationship_wife,
        incident_type_Parked_Car,
        incident_type_Single_Vehicle_Collision,
        incident_type_Vehicle_Theft,
        collision_type_Rear_Collision,
        collision_type_Side_Collision,
        collision_type_Unknown,
        incident_severity_Minor_Damage,
        incident_severity_Total_Loss,
        incident_severity_Trivial_Damage,
        authorities_contacted_Fire,
        authorities_contacted_None,
        authorities_contacted_Other,
        authorities_contacted_Police,
        incident_state_NY,
        incident_state_OH,
        incident_state_PA,
        incident_state_SC,
        incident_state_VA,
        incident_state_WV,
        incident_city_Columbus,
        incident_city_Hillsdale,
        incident_city_Northbend,
        incident_city_Northbrook,
        incident_city_Riverwood,
        incident_city_Springfield,
        property_damage_Unknown,
        property_damage_YES,
        police_report_available_Unknown,
        police_report_available_YES
        ]])
        
    print("===========================================")
    print('months_as_customer: '+months_as_customer,'-----',
        'age: '+age,'-----',
        'policy_csl: '+policy_csl,'-----',
        'policy_deductable:'+policy_deductable,'-----',
        'policy_annual_premium: '+policy_annual_premium,'-----',
        'umbrella_limit: '+umbrella_limit,'-----',
        'insured_sex: '+str(insured_sex),'-----',
        'insured_education_level: '+str(insured_education_level),'-----',
        'capital_gains: '+capital_gains,'-----',
        'capital_loss: '+capital_loss,'-----',
        'incident_hour_of_the_day:'+incident_hour_of_the_day,'-----',
        'number_of_vehicles_involved: '+number_of_vehicles_involved,'-----',
        'bodily_injuries: '+bodily_injuries,'-----',
        "witnesses: "+witnesses,'-----',
        'total_claim_amount: '+total_claim_amount,'-----',
        'injury_claim: '+injury_claim,'-----',
        'property_claim: '+property_claim,'-----',
        'vehicle_claim: '+vehicle_claim,'-----',
        'auto_year: '+auto_year,'-----',
        'policy_state: '+str(policy_state_IN),
        policy_state_OH,'-----',
        'insured_occupation: '+str(insured_occupation_armed_forces),
        insured_occupation_craft_repair,
        insured_occupation_exec_managerial,
        insured_occupation_farming_fishing,
        insured_occupation_handlers_cleaners,
        insured_occupation_machine_op_inspct,
        insured_occupation_other_service,
        insured_occupation_priv_house_serv,
        insured_occupation_prof_specialty,
        insured_occupation_protective_serv,
        insured_occupation_sales,
        insured_occupation_tech_support,
        insured_occupation_transport_moving,'-----',
        'insured_relationship:'+str(insured_relationship_not_in_family),
        insured_relationship_other_relative,
        insured_relationship_own_child,
        insured_relationship_unmarried,
        insured_relationship_wife,'-----',
        'incident_type: '+str(incident_type_Parked_Car),
        incident_type_Single_Vehicle_Collision,
        incident_type_Vehicle_Theft,
        'collision_type: '+str(collision_type_Rear_Collision),
        collision_type_Side_Collision,
        collision_type_Unknown,'-----',
        'incident_severity: '+str(incident_severity_Minor_Damage),
        incident_severity_Total_Loss,
        incident_severity_Trivial_Damage,'-----',
        'authorities_contacted: '+str(authorities_contacted_Fire),
        authorities_contacted_None,
        authorities_contacted_Other,
        authorities_contacted_Police,'-----',
        'incident_state:'+str(incident_state_NY),
        incident_state_OH,
        incident_state_PA,
        incident_state_SC,
        incident_state_VA,
        incident_state_WV,'-----',
        'incident_city: '+str(incident_city_Columbus),
        incident_city_Hillsdale,
        incident_city_Northbend,
        incident_city_Northbrook,
        incident_city_Riverwood,
        incident_city_Springfield,'-----',
        'property_damage: '+str(property_damage_Unknown),
        property_damage_YES,'-----',
        'police_report_available: '+str(police_report_available_Unknown),
        police_report_available_YES)
    print("===============================")
    if prediction==1:
        prediction="This claim is Fraud !!"
    else:
        prediction="This is a Genuine claim !"
            
    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    clf = joblib.load(r"C:\Users\JaisoN\Web_app\Fraud_rf.pkl")
    app.run(port=5000)

