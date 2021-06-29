<script>
import SVG from '@yapv/svg';

export default {
	functional: true,
	render (h, context) {
		const LabelComponent = SVG.circular.LabelComponent(h);
    return LabelComponent(context.props, context.children);
	}
}
</script>
