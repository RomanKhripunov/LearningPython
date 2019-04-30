###################################################################################################
# COPIED FROM INTERNET
###################################################################################################
from bisect import bisect_left


def find_missing(int_array, min_val = False, max_val = False):
    if len(int_array) == 0:
        return list(range(min_val, max_val+1))

    int_array = sorted(int_array)
    first_in_int_array = int_array[0]
    last_in_int_array = int_array[len(int_array)-1]

    if not min_val:
        min_val = first_in_int_array

    if not max_val:
        max_val = last_in_int_array
    result = []

    if min_val < first_in_int_array:
        int_array.insert(0, min_val)
        result.append(min_val)

    if max_val > last_in_int_array:
        int_array.insert(len(int_array), max_val)
        result.append(max_val)

    try:
        min_pos = int_array.index(min_val)

    except Exception as e:
        result.append(min_val)
        min_pos = bisect_left(int_array, min_val)
        int_array.insert(min_pos, min_val)

    try:
        max_pos = int_array.index(max_val)
    except Exception as e:
        result.append(max_val)
        max_pos = bisect_left(int_array, max_val)
        int_array.insert(max_pos, max_val)

    for i in range(min_pos,max_pos):
        difference = int_array[i+1] - int_array[i]
        if difference != 1 and difference != 0:
          result += range(int_array[i]+1,int_array[i+1])

    result.sort()
    return result
###################################################################################################


import re


selected_ids = """276480 278105 517200 291990 315439 605 604 338928 14485 528 14494 14492 14493 14486 14483 14490 345724 345725 137573 137570 355640 137574 366492 246642 247843 247840 276489 276488 278096 259625 255840 255838 255839 259968 255887 367963 29642 14518 14517 14514 14512 14511 14510 14509 14507 53937 29643 15576 523177 523186 229164 255890 255842 632243 53938 53939 15580 349351 349339 349358 349336 291991 291992 291995 315437 315438 319978 291993 647474 608929 137576 523181 523182 414054 247839 423176 423180 423182 423183 291994 423177 319980 319977 731314 255841 367979 367980 367995 414052 368002 368003 368004 14475 14477 14476 14478 14480 349387 542765 542766 349391 349400 349402 542785 349403 349375 397236 349383 543337 542768 349386 349371 349385 450328 450329 450330 450331 450332 450333 543338 452640 484677 456119 459100 456118 504747 459101 467812 530658 467813 467814 467815"""

settings = """select label_159='test_compensate_ammo_after_upgrade' label_157='test_info_screen' label_05='test_buy_equipment_not_enough_money' label_151='test_upgrade_purchased_tank' label_07='test_buy_equipment' label_09='test_open_all_equipment' label_155='test_cancel_upgrade' label_153='test_not_enough_gold_in_modules_screen' data_33='53937' label_85='test_booster_amount_display' data_35='29643' label_87='test_change_installed_booster' label_01='test_install_additional_equipment' label_89='test_get_boosters_in_shop' label_03='test_install_equipment_after_tank_rebuy' data_31='14507' data_37='15576' label_81='test_set_in_slot' data_39='14485' label_83='test_uninstall_booster' label_169='test_sell_ammo' data_159='319978' label_163='test_not_autobuy_ammo' label_161='test_instant_upgrade_cost_changing' label_167='test_buy_ammo' label_165='test_autobuy_ammo' data_43='523177' label_75='test_autobuy_provisions_in_same_slots' data_161='291993' data_45='523186' label_77='test_replacing_provisions' label_79='test_install_booster' data_41='14486' data_169='731314' data_167='14494' data_47='137573' label_71='test_buying_provisions' data_165='14493' data_49='137574' label_73='test_selling_provisions' data_163='14492' label_137='test_not_enough_gold' label_135='test_upgrade_button_missed' data_109='349358' data_107='349339' label_139='test_instant_upgrade_premium_tank' data_105='349351' label_27='test_all_tanks_deselect' label_29='test_select_all_checkbox' label_133='test_upgrade_button_missed_for_1st_lvl_tanks' label_131='test_change_consumables_without_credits' data_55='605' label_21='test_not_enough_gold' data_57='604' label_23='test_exp_field_rounding' data_51='14490' label_25='test_max_exp_limit' data_53='367963' data_113='291990' data_111='349336' data_59='528' label_149='test_upgrade_not_purchased_tank' label_147='test_upgrade_tank_with_different_cost_modules' display='prompt' label_17='test_exchange_exp_update' label_141='test_instant_upgrade_after_manual_upgraded_module' label_19='test_no_elite_tanks' label_145='test_upgrade_tank_with_same_xp_cost_modules' label_143='test_upgrade_button_after_buy' data_65='14483' label_97='test_buy_premium_account' label_11='test_check_no_influence_on_ttx' data_67='247840' label_99='test_buy_360_premium' label_13='test_buy_premium_tank_on_vehicle_tab' data_61='276489' label_15='test_exchange_exp' data_63='345725' valueSeparator=' ' data_103='15580' label_91='test_boosters_in_training_room' data_101='53939' data_69='345724' label_93='test_boosters_in_battle' label_95='test_boosters_decrease_cooldown' label_115='test_no_upgrade_button_for_unresearched_tanks' label_113='test_no_upgrade_button_for_1st_lvl_tanks' label_119='test_cancel_dialog_after_ammo_changes' data_129='414054' label_117='test_upgrade_not_purchased_premium_tank' data_127='523182' label_49='test_not_autobuy_provisions' data_71='137570' label_111='test_disable_camo_button_for_unrepaired_tank' label_41='test_no_autobuy_consumables' data_77='247843' label_43='test_available_consumables_slots' data_79='255838' label_45='test_available_provisions_slots' data_73='355640' label_47='test_autobuy_provisions' data_75='366492' data_135='423180' data_133='423176' data_131='247839' label_127='test_not_enough_credits_for_auto_buying_large_repair_kit' data_119='647474' label_125='test_auto_buying_large_repair_kit' data_117='338928' data_115='315439' label_129='test_change_consumables_without_credits' label_39='test_autobuy_consumables' data_81='255841' label_123='test_adrenalin_not_available_for_auto_guns' label_121='test_confirm_dialog_after_ammo_changes' label_31='test_exp_available_for_conversion' data_87='255842' data_01='276488' label_33='test_not_enough_gold' data_89='259968' label_35='test_gold_exchange' data_83='255839' label_37='test_balance_and_exchange_rate' data_85='255840' data_07='278105' data_125='523181' data_09='517200' data_123='137576' data_03='278096' data_121='608929' data_05='276480' data_149='291991' data_91='259625' description='List of testcaes Ids from TestRail' data_93='255887' data_11='229164' label_63='test_selling_consumables' data_99='53938' data_13='246642' label_65='test_buying_consumables' label_67='test_replacing_consumables' data_95='255890' label_69='test_autobuy_consumables_in_same_slots' data_97='632243' data_19='14517' data_157='315438' data_155='315437' data_15='29642' data_153='291995' data_17='14518' label_61='test_equipment_info' data_151='291992' label_105='test_open_different_screens_from_camouflages' label_103='test_extend_premium' data_139='423183' label_109='test_not_enough_gold' data_137='423182' label_107='test_preview_button' multiple='true' label='Testcases' label_101='test_buy_premium_not_enough_gold' data_21='14514' label_53='test_skills_upgrade' data_23='14512' label_55='test_premium_tank_crew' label_57='test_first_lvl_tank_crew' label_59='test_train_crew_price' data_29='14509' data_147='319977' data_145='319980' data_25='14511' data_143='423177' data_27='14510' label_51='test_info_about_shell' data_141='291994' label_2='test_skills_acceleration_button' data_2='367979' label_4='test_skills_train_button' data_4='367980' label_6='test_fully_upgrade_skill' data_6='367995' label_8='test_train_container_skills' data_8='414052' label_10='test_free_train' data_10='368002' label_12='test_credits_train' data_12='368003' label_14='test_gold_train' data_14='368004' label_16='test_tank_slot_presence' data_16='14475' label_18='test_purchase_slot_screen' data_18='14477' label_20='test_filter_on_slot' data_20='14476' label_22='test_slot_purchase' data_22='14478' label_24='test_not_enough_gold' data_24='14480' label_30='test_sell_gold_camo' data_30='349387' label_32='test_unlock_for_credits' data_32='542765' label_34='test_not_enough_credits' data_34='542766' label_36='test_sell_tank_with_camos' data_36='349391' label_38='test_change_free_camo' data_38='349400' label_40='test_resupply_turned_on' data_40='349402' label_42='test_resupply_turned_on_wrong_camo' data_42='542785' label_44='test_resupply_turned_off' data_44='349403' label_46='test_cant_install_locked_camo' data_46='349375' label_48='test_unlock_camo_with_prem_acc' data_48='397236' label_50='test_camo_slots_behaviour' data_50='349383' label_52='test_camo_selection_behaviour' data_52='543337' label_54='test_camo_selling' data_54='542768' label_56='test_install_free_camo' data_56='349386' label_58='test_unlock_for_gold' data_58='349371' label_60='test_buy_camo' data_60='349385' label_62='test_hud_at_start' data_62='450328' label_64='test_hide_hud_double_tap' data_64='450329' label_66='test_replay_rewind_buttons' data_66='450330' label_68='test_replay_rewind_slider' data_68='450331' label_70='test_exit_replay' data_70='450332' label_72='test_pause_replay' data_72='450333' label_74='test_damage_counters' data_74='543338' label_76='test_after_replay_end' data_76='452640' label_78='test_replay_record' data_78='484677' label_80='test_delete_replay_confirmation' data_80='456119' label_82='test_favourite_tab' data_82='459100' label_84='test_record_selection' data_84='456118' label_86='test_start_selected_replay' data_86='504747' label_88='test_add_replay_to_favourite' data_88='459101' label_90='test_no_record' data_90='467812' label_92='test_no_replay_dialog' data_92='530658' label_94='test_replay_record_limit' data_94='467813' label_96='test_decrease_replay_limit' data_96='467814' label_98='test_limit_not_applied_to_favourites' data_98='467815''"""

new_values = (
    ('test_tank_slot_presence', '14475'),
    ('test_purchase_slot_screen', '14477'),
    ('test_filter_on_slot', '14476'),
    ('test_slot_purchase', '14478'),
    ('test_not_enough_gold', '14480'),
)

all_ids = re.findall(r'\d+', selected_ids)
all_labels = re.findall(r'label\_\d+', settings)
all_datas = re.findall(r'data\_\d+', settings)
all_data_ids = re.findall(r'[\'|\"](\d+)[\'|\"]', settings)


if len(all_labels) != len(all_datas):
    raise Exception('Len of two lists is different: all_labels=%d, all_datas=%d'.format(len(all_labels), len(all_datas)))

numbers = [int(label.split('_')[1]) for label in all_labels]
missed_numbers = find_missing(numbers, min_val=1, max_val=max(numbers))

new_settings = []
new_ids = []
for test_name, test_id in new_values:
    try:
        free_number = missed_numbers.pop(0)
    except IndexError:
        free_number = max(numbers) + 1
        numbers.append(free_number)

    if test_id not in all_data_ids:
        new_settings.append("label_%d='%s' data_%d='%s'" % (free_number, test_name, free_number, test_id))
    else:
        print('-------------- ' + test_id + ' - ' + test_name + ' -------------')

    if test_id not in all_ids:
        new_ids.append(test_id)


new_ids_str = ' '.join(new_ids)
print('-------------- GOT = ' + str(len(new_values)) + '; EDDED = ' + str(len(new_ids)) + ' --------------')
print(selected_ids + ' ' + new_ids_str)

new_settings_str = ' '.join(new_settings)
print('-------------- GOT = ' + str(len(new_values)) + '; EDDED = ' + str(len(new_settings)) + ' --------------')
print(settings + ' ' + new_settings_str)

print('--------------------------------------------------------------------------------------------------')
