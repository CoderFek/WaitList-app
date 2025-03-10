from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404

from .models import WaitListEntry
from .schemas import WaitlistEntryListSchema, WaitlistEntryDetailSchema

router = Router()

@router.get("", response=List[WaitlistEntryListSchema])
def list_waitlist_entries(request):
    qs = WaitListEntry.objects.all()
    return qs

@router.get("{entry_id}/", response=WaitlistEntryDetailSchema)
def get_waitlist_entry(request, entry_id:int):
    obj = get_object_or_404(WaitListEntry ,id=entry_id)
    return obj