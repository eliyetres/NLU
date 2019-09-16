concrete time_sem of time = TDM_sem, Integers_sem ** open Utils_sem in {

lincat

Predicate_minute_to_set = SS;
Predicate_current_time = SS;
Sort_domain = SS;
Sort_string = SS;
Predicate_hour_to_set = SS;
Sort_alarm_time = SS;
Predicate_selected_alarm_time = SS;
Sort_integer = SS;
Predicate_current_alarm = SS;
Unknown = SS;

lin

top = pp "top";
set_time = pp "set_time";
set_time_request_1 hour_to_set = request (pp "set_time") hour_to_set;
set_time_request_2 hour_to_set minute_to_set = request (pp "set_time") hour_to_set minute_to_set;
up = pp "up";
set_alarm = pp "set_alarm";
set_alarm_request_3 selected_alarm_time = request (pp "set_alarm") selected_alarm_time;
eight_thirty = pp "eight_thirty";
nine = pp "nine";
eight = pp "eight";
alarm_off = pp "alarm_off";
hour_to_set = pp "hour_to_set";
hour_to_set_sys_answer individual = pp "hour_to_set" individual;
hour_to_set_propositional_usr_answer answer = pp hour_to_set.s answer;
hour_to_set_sortal_usr_answer answer = answer;
current_time = pp "current_time";
current_time_resolve_ynq_4 = resolve_ynq current_time;
ask_current_time = ask_whq current_time;
current_time_sys_answer_0 = pp "current_time" string_constant_0;
current_time_sys_answer_1 = pp "current_time" string_constant_1;
current_time_sys_answer_2 = pp "current_time" string_constant_2;
current_time_sys_answer_3 = pp "current_time" string_constant_3;
current_time_sys_answer_4 = pp "current_time" string_constant_4;
current_time_sys_answer_5 = pp "current_time" string_constant_5;
current_time_sys_answer_6 = pp "current_time" string_constant_6;
current_time_sys_answer_7 = pp "current_time" string_constant_7;
current_time_sys_answer_8 = pp "current_time" string_constant_8;
current_time_sys_answer_9 = pp "current_time" string_constant_9;
current_time_sortal_usr_answer answer = answer;
current_time_propositional_usr_answer answer = pp current_time.s (ss ("\"" ++ answer.s ++ "\""));
current_alarm = pp "current_alarm";
current_alarm_resolve_ynq_5 = resolve_ynq current_alarm;
ask_current_alarm = ask_whq current_alarm;
current_alarm_sys_answer individual = pp current_alarm.s individual;
current_alarm_sortal_usr_answer answer = answer;
current_alarm_propositional_usr_answer answer = pp current_alarm.s answer;
alarm_time_user_answer answer = answer;
alarm_time_individual individual = individual;
selected_alarm_time = pp "selected_alarm_time";
selected_alarm_time_sys_answer individual = pp selected_alarm_time.s individual;
selected_alarm_time_sortal_usr_answer answer = answer;
selected_alarm_time_propositional_usr_answer answer = pp selected_alarm_time.s answer;
alarm_time_user_answer answer = answer;
alarm_time_individual individual = individual;
minute_to_set = pp "minute_to_set";
minute_to_set_sys_answer individual = pp "minute_to_set" individual;
minute_to_set_propositional_usr_answer answer = pp minute_to_set.s answer;
minute_to_set_sortal_usr_answer answer = answer;
unknown_string unknown = ss ("\"" ++ unknown.s ++ "\"");
mkUnknown string = ss string.s;
report_ended_SetTime_6 hour_to_set minute_to_set = report_ended "SetTime" (list hour_to_set minute_to_set);
report_failed_SetTime_undefined_failure_7 hour_to_set minute_to_set = report_failed "SetTime" (list hour_to_set minute_to_set) "undefined_failure";
report_ended_SetAlarm_8 selected_alarm_time = report_ended "SetAlarm" (list selected_alarm_time);
report_failed_SetAlarm_undefined_failure_9 selected_alarm_time = report_failed "SetAlarm" (list selected_alarm_time) "undefined_failure";
}
