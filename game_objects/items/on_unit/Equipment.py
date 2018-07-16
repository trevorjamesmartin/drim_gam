from game_objects.items import StandardSlots, SlotTypes


class Equipment:
    def __init__(self):
        self.contents = StandardSlots.get_standard_slots()
        self.map = {slot.name : slot for slot in self.contents}
        self.slots_per_type = {st:[] for st in SlotTypes}
        for slot in self.contents:
            type = slot.item_type
            self.slots_per_type[type].append(slot)

    def remove_item(self, slot):
        return slot.take_content()

    def __setitem__(self, slot_name, item):
        self.map[slot_name].content = item

    def __getitem__(self, slot_name):
        return self.map[slot_name].content

    def equip(self, slot_from):
        """
        Choose a fitting slot, and exchange items with it.
        :param item: 
        :return: 
        """

        item = slot_from.content
        slot_type = item.item_type.slot
        if slot_type is None:
            return False

        all_slots_of_type = self.slots_per_type[slot_type]
        if not all_slots_of_type:
            return False

        empty_slots_of_type = [slot for slot in all_slots_of_type if not slot.content]

        if empty_slots_of_type:
            chosen_slot = empty_slots_of_type[0]
        else:
            chosen_slot = all_slots_of_type[0]

        chosen_slot.swap_item(slot_from)
        return True

