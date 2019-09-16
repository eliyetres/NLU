abstract time = TDM, Integers ** {

cat

Predicate_minute_to_set;
Predicate_current_time;
Sort_domain;
Sort_string;
Predicate_hour_to_set;
Sort_alarm_time;
Predicate_selected_alarm_time;
Sort_integer;
Predicate_current_alarm;
Unknown;

fun

top : VpAction;
set_time : VpAction;
set_time_request_1 : Predicate_hour_to_set -> UsrRequest;
set_time_request_2 : Predicate_hour_to_set -> Predicate_minute_to_set -> UsrRequest;
up : VpAction;
set_alarm : VpAction;
set_alarm_request_3 : Predicate_selected_alarm_time -> UsrRequest;
eight_thirty : Sort_alarm_time;
nine : Sort_alarm_time;
eight : Sort_alarm_time;
alarm_off : Sort_alarm_time;
hour_to_set : Predicate;
hour_to_set_sys_answer : Integer -> SysAnswer;
hour_to_set_propositional_usr_answer : Integer -> Predicate_hour_to_set;
hour_to_set_sortal_usr_answer : Integer -> UsrAnswer;
current_time : Predicate;
current_time_resolve_ynq_4 : SysResolveGoal;
ask_current_time : UsrWHQ;
current_time_sys_answer_0 : SysAnswer;
current_time_sys_answer_1 : SysAnswer;
current_time_sys_answer_2 : SysAnswer;
current_time_sys_answer_3 : SysAnswer;
current_time_sys_answer_4 : SysAnswer;
current_time_sys_answer_5 : SysAnswer;
current_time_sys_answer_6 : SysAnswer;
current_time_sys_answer_7 : SysAnswer;
current_time_sys_answer_8 : SysAnswer;
current_time_sys_answer_9 : SysAnswer;
current_time_sortal_usr_answer : Sort_string -> UsrAnswer;
current_time_propositional_usr_answer : Unknown -> Predicate_current_time;
current_alarm : Predicate;
current_alarm_resolve_ynq_5 : SysResolveGoal;
ask_current_alarm : UsrWHQ;
current_alarm_sys_answer : Sort_alarm_time -> SysAnswer;
current_alarm_sortal_usr_answer : Sort_alarm_time -> UsrAnswer;
current_alarm_propositional_usr_answer : Sort_alarm_time -> Predicate_current_alarm;
alarm_time_user_answer : Sort_alarm_time -> UsrAnswer;
alarm_time_individual : Sort_alarm_time -> Individual;
selected_alarm_time : Predicate;
selected_alarm_time_sys_answer : Sort_alarm_time -> SysAnswer;
selected_alarm_time_sortal_usr_answer : Sort_alarm_time -> UsrAnswer;
selected_alarm_time_propositional_usr_answer : Sort_alarm_time -> Predicate_selected_alarm_time;
alarm_time_user_answer : Sort_alarm_time -> UsrAnswer;
alarm_time_individual : Sort_alarm_time -> Individual;
minute_to_set : Predicate;
minute_to_set_sys_answer : Integer -> SysAnswer;
minute_to_set_propositional_usr_answer : Integer -> Predicate_minute_to_set;
minute_to_set_sortal_usr_answer : Integer -> UsrAnswer;
mkUnknown : String -> Unknown;
unknown_string : Unknown -> Sort_string;
report_ended_SetTime_6 : SysAnswer -> SysAnswer -> SysReportEnded;
report_failed_SetTime_undefined_failure_7 : SysAnswer -> SysAnswer -> SysReportFailed;
report_ended_SetAlarm_8 : SysAnswer -> SysReportEnded;
report_failed_SetAlarm_undefined_failure_9 : SysAnswer -> SysReportFailed;
}
