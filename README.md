# visitedhomedata

a python script to get clash of clans base data (buildings, obstacles, last_played etc) from a tag without emulator!

![alt_text](https://i.ibb.co/1YZ9HMtH/Screenshot-2026-10-02-051006.png)

## setup

you need python 3.10 or newer. download the latest coc apk, rename it to `coc.apk` and put it in the same directory of the script.

```bash
pip3 install -r requirements.txt
```

tested with coc **18.600.7**. a newer apk might need the script to be updated too (prob wont update if this wont get enough stars)

## usage

```bash
python3 coc_client.py --apk coc.apk --tag "#2PP"
```

it makes a new account every time. if you want to reuse the last saved account:

```bash
python3 coc_client.py --apk coc.apk --tag "#2PP" --reuse
```

## output

example of data you will get:
```json
{"npc_maps_seen":{"bits":[0,0,0,0,0,0,0]},"unlocked_gem_layouts":0,"active_layout":0,"act_l2":0,"layout_state":[0,0,0,0,0,0,0,0,0,0,0,0,0,0],"layout_state2":[0,0,0,0,0,0,0,0,0,0,0,0,0,0],"layout_cooldown":[0,0,0,0,0,0,0,0,0,0,0,0,0,0],"buildings":[{"data":1000001,"id":500000000,"lvl":0,"x":24,"y":23},{"data":1000004,"id":500000001,"lvl":0,"x":23,"y":19,"res_time":6252},{"data":1000000,"id":500000002,"lvl":0,"x":29,"y":22,"units":[]},{"data":1000015,"id":500000003,"lvl":0,"x":21,"y":23},{"data":1000014,"id":500000004,"lvl":0,"locked":true,"x":28,"y":35,"mode":0}],"obstacles":[{"data":8000007,"id":503000000,"x":6,"y":16},{"data":8000007,"id":503000001,"x":4,"y":45},{"data":8000008,"id":503000002,"x":7,"y":9},{"data":8000005,"id":503000003,"x":35,"y":5},{"data":8000006,"id":503000004,"x":18,"y":44},{"data":8000000,"id":503000005,"x":23,"y":4},{"data":8000008,"id":503000006,"x":45,"y":11},{"data":8000005,"id":503000007,"x":43,"y":21},{"data":8000007,"id":503000008,"x":7,"y":4},{"data":8000003,"id":503000009,"x":32,"y":4},{"data":8000004,"id":503000010,"x":45,"y":4},{"data":8000008,"id":503000011,"x":45,"y":45},{"data":8000005,"id":503000012,"x":23,"y":42},{"data":8000003,"id":503000013,"x":32,"y":37},{"data":8000005,"id":503000014,"x":5,"y":32},{"data":8000005,"id":503000015,"x":3,"y":7},{"data":8000005,"id":503000016,"x":4,"y":20},{"data":8000002,"id":503000017,"x":5,"y":37},{"data":8000002,"id":503000018,"x":7,"y":24},{"data":8000002,"id":503000019,"x":10,"y":36},{"data":8000008,"id":503000020,"x":5,"y":43},{"data":8000001,"id":503000021,"x":11,"y":5},{"data":8000001,"id":503000022,"x":26,"y":44},{"data":8000001,"id":503000023,"x":10,"y":43},{"data":8000007,"id":503000024,"x":4,"y":12},{"data":8000004,"id":503000025,"x":3,"y":3},{"data":8000004,"id":503000026,"x":7,"y":29},{"data":8000003,"id":503000027,"x":42,"y":26},{"data":8000005,"id":503000028,"x":38,"y":39},{"data":8000005,"id":503000029,"x":42,"y":14},{"data":8000001,"id":503000030,"x":3,"y":26},{"data":8000001,"id":503000031,"x":42,"y":5},{"data":8000012,"id":503000032,"x":27,"y":33},{"data":8000012,"id":503000033,"x":41,"y":8},{"data":8000010,"id":503000034,"x":31,"y":43},{"data":8000010,"id":503000035,"x":17,"y":4},{"data":8000013,"id":503000036,"x":42,"y":43},{"data":8000013,"id":503000037,"x":26,"y":3},{"data":8000014,"id":503000038,"x":15,"y":42},{"data":8000014,"id":503000039,"x":28,"y":7},{"data":8000006,"id":503000040,"x":43,"y":30},{"data":8000011,"id":503000041,"x":26,"y":37},{"data":8000011,"id":503000042,"x":27,"y":40},{"data":8000000,"id":503000043,"x":30,"y":38},{"data":8000000,"id":503000044,"x":28,"y":38},{"data":8000000,"id":503000045,"x":29,"y":33},{"data":8000007,"id":503000046,"x":26,"y":35},{"data":8000001,"id":503000047,"x":31,"y":34},{"data":8000014,"id":503000048,"x":35,"y":44},{"data":8000005,"id":503000049,"x":42,"y":35},{"data":8000005,"id":503000050,"x":7,"y":40}],"decos":[],"heroFlags":[],"vobjs":[{"data":39000000,"id":508000000,"lvl":0,"x":27,"y":57},{"data":39000002,"id":508000001,"lvl":0,"x":34,"y":54},{"data":39000004,"id":508000002,"lvl":0,"x":61,"y":21},{"data":39000012,"id":508000003,"lvl":0,"x":59,"y":14},{"data":39000014,"id":508000004,"lvl":0,"x":59,"y":19},{"data":39000015,"id":508000005,"lvl":0,"x":59,"y":28},{"data":39000016,"id":508000006,"lvl":0,"x":62,"y":27},{"data":39000017,"id":508000007,"lvl":0,"x":61,"y":29},{"data":39000018,"id":508000008,"lvl":0,"x":62,"y":30},{"data":39000019,"id":508000009,"lvl":0,"x":61,"y":15},{"data":39000020,"id":508000010,"lvl":0,"x":60,"y":27},{"data":39000021,"id":508000011,"lvl":0,"x":60,"y":17},{"data":39000022,"id":508000012,"lvl":0,"x":59,"y":40,"colId":0},{"data":39000023,"id":508000013,"lvl":0,"x":60,"y":33},{"data":39000024,"id":508000014,"lvl":0,"x":47,"y":60},{"data":39000025,"id":508000015,"lvl":0,"x":40,"y":59},{"data":39000032,"id":508000016,"lvl":0,"x":61,"y":14},{"data":39000033,"id":508000017,"lvl":0,"x":61,"y":23},{"data":39000034,"id":508000018,"lvl":0,"x":62,"y":25},{"data":39000035,"id":508000019,"lvl":0,"x":61,"y":14},{"data":39000036,"id":508000020,"lvl":0,"x":60,"y":17},{"data":39000037,"id":508000021,"lvl":0,"x":61,"y":14},{"data":39000038,"id":508000022,"lvl":0,"x":61,"y":16},{"data":39000039,"id":508000023,"lvl":0,"x":61,"y":18},{"data":39000041,"id":508000024,"lvl":0,"x":61,"y":14},{"data":39000043,"id":508000025,"lvl":0,"x":59,"y":14}],"respawnVars":{"secondsFromLastRespawn":1318,"respawnSeed":30281367,"obstacleClearCounter":0,"time_to_gembox_drop":603482,"time_in_gembox_period":0,"time_to_special_drop":31082,"time_to_special_period":302400},"units":{"unit_prod":{}},"spells":{"unit_prod":{}},"siege_machines":{"unit_prod":{}},"buildings2":[{"data":1000033,"id":500000001,"lvl":0,"x":26,"y":23},{"data":1000033,"id":500000002,"lvl":0,"x":24,"y":23},{"data":1000033,"id":500000003,"lvl":0,"x":28,"y":23},{"data":1000033,"id":500000004,"lvl":0,"x":25,"y":23},{"data":1000033,"id":500000005,"lvl":0,"x":27,"y":23},{"data":1000033,"id":500000006,"lvl":0,"x":29,"y":19},{"data":1000033,"id":500000007,"lvl":0,"x":29,"y":17},{"data":1000033,"id":500000008,"lvl":0,"x":29,"y":21},{"data":1000033,"id":500000009,"lvl":0,"x":29,"y":18},{"data":1000033,"id":500000010,"lvl":0,"x":29,"y":20},{"data":1000035,"id":500000011,"lvl":0,"locked":true,"x":20,"y":21,"res_time":0},{"data":1000040,"id":500000012,"lvl":0,"locked":true,"x":17,"y":13,"unit_prod":{"m":1,"unit_type":0}},{"data":1000044,"id":500000013,"lvl":0,"locked":true,"x":25,"y":19},{"data":1000039,"id":500000014,"lvl":0,"locked":true,"x":8,"y":30},{"data":1000053,"id":500000015,"lvl":0,"locked":true,"x":33,"y":8,"hero":{"hero_global_id":28000003}},{"data":1000046,"id":500000016,"lvl":0,"locked":true,"x":15,"y":21},{"data":1000042,"id":500000017,"lvl":0,"locked":true,"x":21,"y":12,"up2":{"slot":1}},{"data":1000037,"id":500000018,"lvl":0,"locked":true,"x":24,"y":14,"res_time":15149},{"data":1000058,"id":500000019,"lvl":0,"locked":true,"x":6,"y":14,"res_time":0},{"data":1000034,"id":500000020,"lvl":0,"x":21,"y":17}],"obstacles2":[{"data":8000042,"id":503000000,"x":33,"y":30},{"data":8000049,"id":503000001,"x":34,"y":16},{"data":8000050,"id":503000002,"x":20,"y":31},{"data":8000050,"id":503000003,"x":34,"y":6},{"data":8000050,"id":503000004,"x":26,"y":27},{"data":8000050,"id":503000005,"x":3,"y":26},{"data":8000041,"id":503000006,"x":6,"y":35},{"data":8000041,"id":503000007,"x":26,"y":34},{"data":8000041,"id":503000008,"x":24,"y":29},{"data":8000041,"id":503000010,"x":35,"y":28},{"data":8000041,"id":503000011,"x":31,"y":7},{"data":8000041,"id":503000012,"x":15,"y":5},{"data":8000041,"id":503000013,"x":7,"y":7},{"data":8000041,"id":503000014,"x":10,"y":16},{"data":8000041,"id":503000015,"x":13,"y":25},{"data":8000041,"id":503000016,"x":16,"y":33},{"data":8000041,"id":503000018,"x":34,"y":35},{"data":8000047,"id":503000021,"x":12,"y":31},{"data":8000047,"id":503000022,"x":9,"y":24},{"data":8000047,"id":503000023,"x":3,"y":8},{"data":8000049,"id":503000024,"x":5,"y":31},{"data":8000049,"id":503000025,"x":17,"y":7},{"data":8000056,"id":503000027,"x":27,"y":4},{"data":8000056,"id":503000028,"x":11,"y":20},{"data":8000055,"id":503000029,"x":20,"y":7},{"data":8000057,"id":503000030,"x":4,"y":3},{"data":8000057,"id":503000031,"x":3,"y":22},{"data":8000057,"id":503000032,"x":10,"y":7},{"data":8000057,"id":503000033,"x":34,"y":3},{"data":8000057,"id":503000034,"x":26,"y":8},{"data":8000057,"id":503000035,"x":29,"y":31},{"data":8000057,"id":503000037,"x":20,"y":26},{"data":8000061,"id":503000038,"x":13,"y":34},{"data":8000062,"id":503000039,"x":29,"y":35},{"data":8000062,"id":503000041,"x":24,"y":5},{"data":8000060,"id":503000042,"x":11,"y":27},{"data":8000060,"id":503000043,"x":3,"y":34},{"data":8000060,"id":503000044,"x":30,"y":3},{"data":8000060,"id":503000045,"x":9,"y":10},{"data":8000059,"id":503000046,"x":7,"y":27},{"data":8000059,"id":503000047,"x":10,"y":35},{"data":8000059,"id":503000053,"x":23,"y":3},{"data":8000059,"id":503000054,"x":18,"y":3},{"data":8000059,"id":503000055,"x":3,"y":20},{"data":8000056,"id":503000058,"x":22,"y":34},{"data":8000056,"id":503000060,"x":7,"y":22},{"data":8000056,"id":503000061,"x":29,"y":12},{"data":8000058,"id":503000062,"x":30,"y":25},{"data":8000058,"id":503000063,"x":31,"y":13},{"data":8000058,"id":503000064,"x":8,"y":4},{"data":8000059,"id":503000065,"x":16,"y":27},{"data":8000051,"id":503000066,"x":16,"y":30},{"data":8000053,"id":503000067,"x":11,"y":4,"lmv":2},{"data":8000044,"id":503000068,"x":24,"y":9,"lmv":2},{"data":8000051,"id":503000069,"x":14,"y":9,"lmv":2},{"data":8000063,"id":503000070,"x":21,"y":10},{"data":8000063,"id":503000071,"x":22,"y":10},{"data":8000063,"id":503000072,"x":23,"y":9},{"data":8000064,"id":503000073,"x":22,"y":6},{"data":8000064,"id":503000074,"x":21,"y":6},{"data":8000063,"id":503000075,"x":23,"y":10},{"data":8000064,"id":503000076,"x":22,"y":11},{"data":8000064,"id":503000077,"x":19,"y":7},{"data":8000064,"id":503000078,"x":19,"y":8},{"data":8000064,"id":503000079,"x":21,"y":11},{"data":8000048,"id":503000080,"x":30,"y":21},{"data":8000048,"id":503000081,"x":28,"y":24},{"data":8000048,"id":503000082,"x":30,"y":20},{"data":8000048,"id":503000083,"x":30,"y":18},{"data":8000048,"id":503000084,"x":25,"y":11},{"data":8000048,"id":503000085,"x":26,"y":12},{"data":8000048,"id":503000086,"x":27,"y":12},{"data":8000060,"id":503000087,"x":33,"y":12},{"data":8000050,"id":503000088,"x":10,"y":13},{"data":8000051,"id":503000089,"x":4,"y":16},{"data":8000053,"id":503000090,"x":7,"y":17},{"data":8000061,"id":503000091,"x":6,"y":12},{"data":8000047,"id":503000092,"x":34,"y":22}],"decos2":[],"heroFlags2":[],"vobjs2":[{"data":39000001,"id":508000000,"lvl":0,"x":9,"y":48},{"data":39000003,"id":508000001,"lvl":0,"x":4,"y":51},{"data":39000028,"id":508000002,"lvl":0,"x":11,"y":59,"colId":0},{"data":39000029,"id":508000003,"lvl":0,"x":58,"y":20},{"data":39000030,"id":508000004,"lvl":0,"x":46,"y":20},{"data":39000031,"id":508000005,"lvl":0,"x":0,"y":0},{"data":39000040,"id":508000006,"lvl":0,"x":11,"y":59}],"v2rs":1318,"v2rseed":112,"v2ccounter":0,"tgsec":1318,"tgseed":0,"cooldowns":[],"newShopBuildings":[0,0,1,1,0,1,1,0,1,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"newShopTraps":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"newShopDecos":[1,4,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"offer":{"offers":[]},"last_alliance_level":1,"last_season_seen":-1,"last_news_seen":-1,"reinforce_using_gems":false,"army_names":["","","","","","",""],"army_presets":[[],[],[],[],[],[],[]],"active_army_loadout":{"m_type":1,"m_customName":"","slots_by_type":[[],[],[],[],[]]},"friendly_army_loadout":{"m_type":3,"m_customName":"","slots_by_type":[[],[],[],[],[]]},"saved_army_loadouts":[{"m_type":2,"m_customName":"","slots_by_type":[[],[],[],[],[]]},{"m_type":2,"m_customName":"","slots_by_type":[[],[],[],[],[]]},{"m_type":2,"m_customName":"","slots_by_type":[[],[],[],[],[]]},{"m_type":2,"m_customName":"","slots_by_type":[[],[],[],[],[]]},{"m_type":2,"m_customName":"","slots_by_type":[[],[],[],[],[]]},{"m_type":2,"m_customName":"","slots_by_type":[[],[],[],[],[]]},{"m_type":2,"m_customName":"","slots_by_type":[[],[],[],[],[]]},{"m_type":2,"m_customName":"","slots_by_type":[[],[],[],[],[]]}],"account_flags":0,"bool_layout_edit_shown_erase":false,"events":[50185,55483,71673,76725,283140,283141,283143,283136,283138,283139,283148,283149,283150,283151,283144,283145,283146,539911,283156,283158,283159,283153,283154,283155,283164,283165,283166,283160,283161,283163,642349,283168,284961,283169,283170,549694,549695,643121,643120,642354,643122,643125,643124,643126,543304,482375,543305,543306,543307,284999,543308,543309,482383,549696,482382,549697,482381,549698,482380,285000,482379,543301,482378,543302,482377,543303,482376,482391,482390,482389,515923,482387,515922,482386,515921,482385,515920,482384,482399,482398,285022,482397,482396,482395,482394,482393,482392,285024,511331,482401,482400,285033,290686,290681,285060,540033,643204,643218,646830,525479,311732,311733,263856,311730,516287,285885,549555,540085,646839,544456,544457,544458,544459,544460,544455,251604,603857,552424,511467,283125,525561,283126,283127,291568,291569,248571,283133,283134,283135,248575,283129,283130,643063,283131],"es":0,"alliance_games":{"last_seen":0,"last_id":-1,"last_end":0,"p_score":0,"p_max":0,"p_reward":0,"a_score":-1,"cooldown":0,"n_cooldown":0,"last_seen_id":-1,"thresholds":[],"rewards":[],"thresholdXP":[],"chosen_indices":[],"chosen_alternates":[],"rewards_claimed":false,"personal_reward_claimed":false,"personal_reward_threshold":-1,"personal_reward_index":-1,"personal_reward_alt":false},"trader":{"event":549555,"seen":false},"battlepass":{"free_rewards":[],"premium_rewards":[],"seasonStartTH":0,"seasonStartBH":0,"lpeTypeMap":[0,0]},"chain_offer":{"chain_offers":[{"event_id":515920,"claimed_steps":[],"event_end_time":1791771451}]},"streak_event":{"m_premiumPurchased":false,"m_hasSeenEventStart":false,"m_currentStreakTier":0,"m_lastTierChangeAttackTimestamp":0,"m_nextResetTime":0,"m_streakBroken":false,"m_streakStartTime":0,"m_tierUnlockOffset":0,"m_streakStateTransition":0,"m_nextUnlockTime":0,"m_streakTaskUnlockSeen":-1},"progress_track_event":{"m_extraTokenRewardAmount":0,"m_cachedActiveEventId":0,"m_eventTrackFinished":false,"m_debugUnlockAllCombatItems":false,"resLastCollected":0,"version":0,"m_eventStartTHLevel":0,"m_eventStartBHLevel":0,"free_rewards":[],"premium_rewards":[]},"crafting_event":{"m_cachedActiveEventId":0,"m_activeEventEndTime":0,"m_eventStartTime":0,"m_nextDailyRefreshTime":0,"m_score":0,"m_premium":false,"m_serveSequenceCounter":0,"m_chosenPrimaryResourceGlobalId":0,"m_seenInfoPopup":false,"m_seenPassUpsell":false,"version":0,"passiveLastCollected":0},"hero_progression":{"score":0,"lastSeenScore":0,"migrated":0,"eventId":0},"reengage":{"last_time":0,"num_times":0,"absence":0,"builder_upgrades":[],"lab_upgrades":[],"version":2,"spl":false},"dailylogin":{},"superlicences":{"licence_ends":[]},"reward_boxes":{"poolSeeds":[],"pools":{}},"intermediate_storage":{},"collection":{"items":[],"archived":[]},"consumable":{},"villagerapprentice":{"apprentice0":{"dataId":93000000,"level":-1,"state":0,"recurrentUsage":false,"seen":false,"targetId":0,"recurrentTargetId":0,"forgeSlot":-1,"recurrentForgeSlot":-1,"m_totalSavedTime":0},"apprentice1":{"dataId":93000001,"level":-1,"state":0,"recurrentUsage":false,"seen":false,"targetId":0,"recurrentTargetId":0,"m_totalSavedTime":0},"apprentice2":{"dataId":93000002,"level":-1,"state":0,"recurrentUsage":false,"seen":false,"targetId":3000001,"amountSelected":50},"apprentice3":{"dataId":93000003,"level":-1,"state":0,"recurrentUsage":false,"seen":false,"targetId":3000019,"amountSelected":50}},"mini_level_manager":{"cnt":0,"m_hasEverSeenInfoScreens":false,"prestigeEarned":0},"guardian_manager":{"m_version":1,"m_seenInfoScreen":false},"last_event_id_store":{"eventIds":[53,248575]},"last_seen_manager":{},"event_reward_track_manager":{},"season_pass_manager":{"activeEventId":0,"activeEventEndTime":0,"passLevel":-1,"completedCards":0,"repeatBuyerBonusCards":0,"lastPremiumEnded":0,"hvBankStartSize":0,"bbBankStartSize":0},"resourceFestBuildingTypes":[],"scenery_clickables_states":{},"scenery_clickable_counters":{"count":0,"clickedLocations":[]},"disableShopPersonalisation":false,"lastNewsStorySeen":0,"last_name_change":0,"creator_tag":"","creator_expiration":0,"last_played":1790908771,"next_th_boost_level":1,"upgradesCompletedAway":[],"forge":[{"fg_id":66000000,"fg_tier":0,"fg_t":0},{},{},{},{},{}],"resourceFestId":0,"anniversaryRewards":[],"exp_ver":2,"migrated_army_loadouts":true,"seasonal_defense":{"endTime":0,"eventId":0,"ineligibleEventID":511331,"upgradeCount":0,"prestigeEarned":0,"seasonalDefenseRemoved":false,"seasonalDefenseRefunded":false,"seasonalDefenseReset":false,"m_seasonalDefenseTutorialFlaggedForReset":false},"bg":[0,0,[0,0]],"layout_edit_timestamps":[0,0,0,0,0,0,0,0,0,0,0,0,0,0],"layout_edit_timestamps_v2":[0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
```
JSON Keys: `npc_maps_seen
unlocked_gem_layouts
active_layout
act_l2
layout_state
layout_state2
layout_cooldown
buildings
obstacles
decos
heroFlags
vobjs
respawnVars
units
spells
siege_machines
buildings2
obstacles2
decos2
heroFlags2
vobjs2
v2rs
v2rseed
v2ccounter
tgsec
tgseed
cooldowns
newShopBuildings
newShopTraps
newShopDecos
offer
last_alliance_level
last_season_seen
last_news_seen
reinforce_using_gems
army_names
army_presets
active_army_loadout
friendly_army_loadout
saved_army_loadouts
account_flags
bool_layout_edit_shown_erase
events
es
alliance_games
trader
battlepass
chain_offer
streak_event
progress_track_event
crafting_event
hero_progression
reengage
dailylogin
superlicences
reward_boxes
intermediate_storage
collection
consumable
villagerapprentice
mini_level_manager
guardian_manager
last_event_id_store
last_seen_manager
event_reward_track_manager
season_pass_manager
resourceFestBuildingTypes
scenery_clickables_states
scenery_clickable_counters
disableShopPersonalisation
lastNewsStorySeen
last_name_change
creator_tag
creator_expiration
last_played
next_th_boost_level
upgradesCompletedAway
forge
resourceFestId
anniversaryRewards
exp_ver
migrated_army_loadouts
seasonal_defense
bg
layout_edit_timestamps
layout_edit_timestamps_v2`

the data gets printed and saved in `client-session`. if that folder already exists, it uses `client-session-001`, `client-session-002` etc.

- `profile_home.json` — the base data
- `avatar_profile.json` — the tag, ids and base data
- `avatar_profile.bin` — the full decrypted response
- `account.json` — the account it used

## timestamps

fields like `last_played` and `last_name_change` are unix timestamps in seconds. they're numbers representing a date and time.

to convert one, go to https://www.unixtimestamp.com/ and paste the number into the timestamp converter.

example: `1704067200` converts to **january 1, 2024 at 00:00:00 utc**.

a value of `0` can mean the field isn't set, so don't assume it means the player actually did something in 1970.

## message ids

these are for coc **18.600.7**:

| id | name |
| --- | --- |
| 10100 | clienthello |
| 20100 | serverhello |
| 10101 | login |
| 23654 | loginok |
| 20103 | loginfailed |
| 25195 | ownhomedata |
| 11734 | askforavatarprofile |
| 26443 | avatarprofile |
| 20206 | avatarprofilefailed |

the script gets the base data from avatarprofile. no emulator needed to run it.

thanks to astra & ghirda for the help
last updated on october 03 2026
