/** Peasy components. Namespace: window.Peasy */
export interface ButtonProps { size?: "L"|"M"|"S"; form?: "full"|"outline"; surface?: "light"|"dark"; iconFront?: boolean; iconBack?: boolean; block?: boolean; href?: string; disabled?: boolean; onClick?: () => void; children: string }
export interface TextLinkProps { size?: "L"|"M"|"S"; surface?: "light"|"dark"; href?: string; children: string }
export interface IconButtonProps { size?: "L"|"M"|"S"; icon?: string; label: string; onClick?: () => void }
export interface TextFieldProps { label: string; placeholder?: string; value?: string; type?: string; required?: boolean; optional?: boolean; disabled?: boolean; focused?: boolean; error?: string; help?: string; orientation?: "vertical"|"horizontal" }
export interface SelectProps { label: string; options: string[]; placeholder?: string; disabled?: boolean; focused?: boolean; error?: string; orientation?: "vertical"|"horizontal" }
export interface TextAreaProps { label: string; placeholder?: string; max?: number; disabled?: boolean }
export interface CheckboxProps { checked?: boolean; disabled?: boolean; children: string }
export interface RadioProps { name: string; checked?: boolean; disabled?: boolean; children: string }
export interface TagProps { children: string }
export interface SelectorPillProps { size?: "L"|"M"|"S"; active?: boolean; onClick?: () => void; children: string }
export interface BadgeProps { children: string }
export interface OfferCardProps { provider: string; price: string; unit?: string; name: string; features: string[]; badge?: string; cta?: string }
export interface PerkCardProps { icon?: string; title: string; text: string; link?: string }
export interface NewsCardProps { image?: string; tag?: string; date: string; title: string; text: string; link?: string }
export interface ContactOptionProps { icon?: string; title: string; text: string }
export interface FAQProps { items: { q: string; a: string }[]; open?: number }
export interface SearchProps { placeholder?: string }
export interface BreadcrumbProps { items: string[] }
export interface UspBarProps { rating?: string; usps: string[]; hours?: string }
export interface IconProps { name: "ArrowRight"|"Check"|"Dropdown"|"MagnifyingGlass"|"House"|"Headset"|"CalendarDots"|"Question"|"PhoneCall"|"PhoneTransfer"|"MapPin"|"Tag"; size?: number; label?: string }
